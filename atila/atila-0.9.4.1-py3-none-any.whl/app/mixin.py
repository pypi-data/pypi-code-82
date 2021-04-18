from functools import wraps
from rs4.termcolor import tc
import os, sys
from importlib import reload
from skitai import was as the_was
import time, threading
from rs4.attrdict import AttrDictTS, AttrDict
import atila
from . import decorators, auth, template_engine, router, events, testutils
from types import ModuleType, FunctionType
import copy
import inspect

class MixIn (
        decorators.Decorators,
        router.Router,
        events.Events,
        auth.Auth,
        template_engine.TemplateEngine,
        testutils.TestUtils
    ):

    # core settings --------------------------------
    debug = False
    use_reloader = False
    enable_namespace = True
    auto_mount = True

    expose_spec = False

    # session and auth -----------------------------
    securekey = None
    session_timeout = None
    access_control_allow_origin = None
    access_control_max_age = 0
    authenticate = None

    # global app objects ----------------------------
    glock = threading.RLock ()

    def __init__ (self):
        decorators.Decorators.__init__ (self)
        router.Router.__init__ (self)
        events.Events.__init__ (self)
        auth.Auth.__init__ (self)
        template_engine.TemplateEngine.__init__ (self)

        self.module = None
        self.packagename = None
        self.wasc = None
        self.logger = None
        self.g = self.store = AttrDictTS ()
        self.lock = threading.RLock ()

        self.mount_p = "/"
        self.path_suffix_len = 0
        self.service_roots = []
        self.mount_params = {}
        self.reloadables = {}
        self.reloadable_objects = {}
        self.last_reloaded = time.time ()
        self.init_time = time.time ()

        self._mount_funcs = []
        self._maintern_funcs = {}
        self._package_dirs = set ()
        self._mount_option = {}
        self._started = False
        self._current_mount_options = None

        self._salt = None

        self.g ["__last_maintern"] = 0.0
        self.g ["__maintern_count"] = 0
        self._locks = {}

    @property
    def r (self):
        return AttrDict ()

    def get_lock (self, name = None):
        if name is None:
            return self.lock
        with self.lock:
            lock = self._locks.get (name)
            if lock is None:
                lock = self._locks [name] = threading.RLock ()
        return lock

    def maintern (self):
        # called from wsgi_executeor.find_method ()
        if not self._maintern_funcs:
            return

        now = time.time ()
        if (now - self.g ["__last_maintern"]) < self.config.MAINTAIN_INTERVAL:
            return

        was = the_was._get ()
        with self.lock:
            for func, interval, threading in self._maintern_funcs.values ():
                count = self.g ["__maintern_count"]
                if count % interval != 0:
                    continue
                if threading:
                    was.Thread (func, args = (was, now, count))
                else:
                    func (was, now, count)
        self.g ["__last_maintern"] = now
        self.g ["__maintern_count"] = count + 1

    def get_resource (self, *args):
        return self.joinpath ("resources", *args)

    def joinpath (self, *args):
        return os.path.normpath (os.path.join (self.home, *args))

    def set_mount_point (self, mount):
        if not mount or mount == '/':
            self.mount_p = "/"
        elif mount [-1] != "/":
            self.mount_p = mount + "/"
        else:
            self.mount_p = mount
        self.path_suffix_len = len (self.mount_p) - 1

    def init (self, module, packagename = "app", mount = "/"):
        self.module = module
        self.packagename = packagename
        self.set_mount_point (mount)

        if self.module:
            self.abspath = self.module.__file__
            if self.abspath [-3:] != ".py":
                self.abspath = self.abspath [:-1]
            self.update_file_info    ()

    def __getitem__ (self, k):
        return self.route_map [k]

    def get_file_info (self, module):
        stat = os.stat (module.__file__)
        return stat.st_mtime, stat.st_size

    def update_file_info (self):
        stat = os.stat (self.abspath)
        self.file_info = (stat.st_mtime, stat.st_size)

    #------------------------------------------------------
    @property
    def salt (self):
        if self._salt:
            return self._salt
        if not self.securekey:
            self._salt = None
        else:
            self._salt = self.securekey.encode ("utf8")
        return self._salt

    def set_default_session_timeout (self, timeout):
        self.session_timeout = timeout

    def set_devel (self, debug = True, use_reloader = True):
        self.debug = debug
        self.use_reloader = use_reloader

    # services management ----------------------------------------------
    PACKAGE_DIRS = ["services", "exports"]
    def add_package (self, *names):
        for name in names:
            self.PACKAGE_DIRS.append (name)

    MOUNT_HOOKS = ["__mount__", "mount"]
    UMOUNT_HOOKS = ["__umount__", "umount", "dettach"]
    def _mount (self, module):
        mount_func = None
        for hook in self.MOUNT_HOOKS:
            if hasattr (module, hook):
                mount_func = getattr (module, hook)
                break

        if mount_func:
            if not self.auto_mount and module not in self.mount_params:
                return
            params = self.mount_params.get (module, {})
            if params.get ("debug_only") and not self.debug:
                return
            params ["module_name"] = module.__name__
            if self.enable_namespace and "ns" not in params:
                if module.__name__ not in self.PACKAGE_DIRS:
                    try:
                        _, ns = module.__name__.split (".", 1)
                        if _ not in self.PACKAGE_DIRS:
                            ns = module.__name__
                    except ValueError:
                        ns = module.__name__
                    params ["ns"] = ns
            setattr (module, "__mntopt__", params)
            # for app initialzing and reloading
            self._mount_option = params

            fspec = inspect.getfullargspec (mount_func)
            try:
                if len (fspec.args) == 1:
                    mount_func (self)
                else:
                    mount_func (self, params)
                if 'point' in params:
                    self.log ("- {} mounted to {}".format (module.__name__, tc.white (self.mount_p [:-1] + params ['point'])), "info")
                else:
                    self.log ("- {} mounted".format (module.__name__), "info")
            finally:
                self._mount_option = {}

        try:
            self.reloadables [module] = self.get_file_info (module)
        except FileNotFoundError:
            del self.reloadables [module]
            return

        # find recursively
        self.find_mountables (module)

    def _reload_objects (self, origin):
        if origin not in self.reloadable_objects:
            return

        deletables = []
        for objname, includers in self.reloadable_objects [origin].items ():
            for each in includers:
                try:
                    attr = getattr (origin, objname)
                except AttributeError:
                    deletables.append (objname)
                    continue
                setattr (each, objname, attr)

        for objname in deletables:
            try:
                del self.reloadable_objects [origin][objname]
            except KeyError:
                pass

    def _set_reloadable_object (self, objname, origin, includer):
        if origin not in self.reloadable_objects:
            self.reloadable_objects [origin] = {}
        if objname not in self.reloadable_objects [origin]:
            self.reloadable_objects [origin][objname] = set ()
        self.reloadable_objects [origin][objname].add (includer)

    def get_modpath (self, module):
        try:
            modpath = module.__spec__.origin
        except AttributeError:
            try:
                modpath = module.__file__
            except AttributeError:
                return
        return modpath

    def find_mountables (self, module):
        for attr in dir (module):
            if attr.startswith ("__"):
                continue
            v = getattr (module, attr)
            maybe_object = None
            mountable = False

            if hasattr (v, "__module__"):
                maybe_object = attr
                try:
                    v = sys.modules [v.__module__]
                    if v == module:
                        continue
                except KeyError:
                    continue

            if type (v) is not ModuleType:
                continue

            modpath = self.get_modpath (v)
            if not modpath:
                continue

            maybe_object and self._set_reloadable_object (maybe_object, v, module)
            if v in self.reloadables:
                continue

            if v in self.reloadables:
                continue

            for package_dir in self._package_dirs:
                if modpath.startswith (package_dir):
                    mountable = True
                    break

            if mountable:
                self._mount (v)

    def add_package_dir (self, path):
        for exist in self._package_dirs:
            if exist.startswith (path) and len (path) > len (exist):
                return
        self._package_dirs.add (path)

    def mount_explicit (self):
        for module in self.mount_params:
            if module in self.reloadables:
                continue
            self._mount (module)

    def mount_funcs (self):
        for mount_func, params in self._mount_funcs:
            fspec = inspect.getfullargspec (mount_func)
            if len (fspec.args) == 1:
                mount_func (self)
            else:
                mount_func (self, params)
            if 'point' in params:
                self.log ("- {} mounted to {}".format (mount_func.__name__, tc.white (self.mount_p [:-1] + params ['point'])), "info")
            else:
                self.log ("- {} mounted".format (mount_func.__name__), "info")

    def mount_nested (self):
        # within __mount__
        for module in list (sys.modules.values ()):
            if module in self.reloadables:
                continue
            modpath = self.get_modpath (module)
            if not modpath:
                continue
            for package_dir in self._package_dirs:
                if modpath.startswith (package_dir):
                    self._mount (module)
                    break

    def mount (self, maybe_point = None, *modules, **kargs):
        self.auto_mount = False # set to explicit mount mode
        if maybe_point or maybe_point == '':
            if isinstance (maybe_point, str):
                kargs ["point"] = maybe_point
            else:
                modules = (maybe_point,) + modules

        kargs ["point"] = kargs ["point"]
        if self._current_mount_options:
            # called in __setup__ hook, make sure sub path mount
            kargs ['point'] = self._current_mount_options ['point'] + kargs ['point']
            if kargs ['point'].endswith ('//'):
                kargs ['point'] = kargs ['point'][:-1]
            if kargs ['point'].startswith ('//'):
                kargs ['point'] = kargs ['point'][1:]

        for module in modules:
            setup_func = None
            if isinstance (module, FunctionType):
                self._mount_funcs.append ((module, copy.copy (kargs)))
                continue

            try:
                setup_func = getattr (module, '__setup__')
            except AttributeError:
                pass
            else:
                self._current_mount_options = kargs
                fspec = inspect.getfullargspec (setup_func)
                try:
                    if len (fspec.args) == 1:
                        setup_func (self)
                    else:
                        setup_func (self, copy.copy (kargs))
                finally:
                    self._current_mount_options = None

            mount_func = None
            for hook in self.MOUNT_HOOKS:
                if hasattr (module, hook):
                    mount_func = getattr (module, hook)
                    break

            if not setup_func:
                assert mount_func, "__mount__ hook doesn't exist"

            if mount_func:
                self.add_package_dir (os.path.dirname (self.get_modpath (module)))
                self.mount_params [module] = (copy.copy (kargs))

    mount_with = decorate_with = mount

    def umount (self, *modules):
        for module in modules:
            umount_func = None
            for hook in self.UMOUNT_HOOKS:
                if hasattr (module, hook):
                    umount_func = getattr (module, hook)
                    break
            if not umount_func:
                return
            umount_func (self)
            self.log ("- %s umounted" % module.__name__, "info")

    def umount_all (self):
        self.umount (*tuple (self.reloadables.keys ()))
    dettach_all = umount_all

    def _reload (self):
        reloaded = 0
        for module in list (self.reloadables.keys ()):
            try:
                fi = self.get_file_info (module)
            except FileNotFoundError:
                del self.reloadables [module]
                continue
            if self.reloadables [module] == fi:
                continue
            self.log ("- reloading service, %s" % module.__name__, "info")
            for each in self.service_roots:
                # reinstead package root for path finder
                sys.modules [each.__name__] = each
            try:
                newmodule = reload (module)
            except:
                self.log ("- reloading failed. see exception log, %s" % module.__name__, "fatal")
                raise

            reloaded += 1
            self._current_function_specs = {}
            self.umount (module)
            del self.reloadables [module]
            self._mount (newmodule)
            self._reload_objects (newmodule)
        return reloaded

    def maybe_reload (self):
        with self.lock:
            if self._reloading or time.time () - self.last_reloaded < 1.0:
                return
            self._reloading = True

        try:
            self._reload () and self.load_jinja_filters ()
        finally:
            with self.lock:
                self.last_reloaded = time.time ()
                self._reloading = False

    # logger ----------------------------------------------------------
    def set_logger (self, logger):
        self.logger = logger

    def log (self, msg, type = "info"):
        if self.logger is None:
            if type != 'info':
                raise SystemError ('[{}] {}'.format (type, msg))
        self.logger (msg, type)

    def traceback (self):
        self.logger.trace ()
    trace = traceback

    PHASES = {
        'before_mount': 0,
        'mounted': 3,
        'before_reload': 5,
        'reloaded': 1,
        'before_umount': 4,
        'umounted': 2,
        'mounted_or_reloaded': 6
    }
    def life_cycle (self, phase, obj):
        self.bus.emit (phase)
        if phase in ("umounted", "before_reload"):
            self.umount_all ()
        index = self.PHASES.get (phase)
        func = self._binds_server [index]
        if not func:
            return

        obj.app = self
        try:
            func (obj)
        except:
            if self.logger:
                self.logger.trace ()
            else:
                raise

    # Error handling ------------------------------------------------------
    def render_error (self, error, was = None):
        handler = self.handlers.get (error ['code'], self.handlers.get (0))
        if not handler:
            return
        was = was or the_was._get ()
        if not hasattr (was, "response") or was.response is None:
            return
        # reset was.app for rendering
        was.app = self
        content =  handler [0] (was, error)
        was.app = None
        return content


    # app startup and shutdown --------------------------------------------
    def cleanup (self):
        pass

    def _start (self, wasc, route, reload = False):
        self.wasc = wasc
        if not route:
            self.basepath = "/"
        elif not route.endswith ("/"):
            self.basepath = route + "/"
        else:
            self.basepath = route

    def start (self, wasc, route):
        self._start (wasc, route)
        self._started = True

    def restart (self, wasc, route):
        self._reloading = True
        self._start (wasc, route, True)
        self._reloading = False

