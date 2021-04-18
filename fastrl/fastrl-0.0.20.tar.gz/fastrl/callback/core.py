# AUTOGENERATED! DO NOT EDIT! File to edit: nbs/03_callback.core.ipynb (unless otherwise specified).

__all__ = ['Loop', 'loop_event', 'LoopCallback']

# Cell
# Python native modules
import os
from typing import *
# Third party libs
from fastcore.all import *
from fastai.callback.core import *
from fastai.data.all import *
# Local modules

# Cell
defaults.loop_callbacks=L()

_loop = ['Start Fit', 'before_fit', 'Start Epoch Loop', 'before_epoch', 'Start Train', 'before_train',
         'Start Batch Loop', 'before_batch', 'after_pred', 'after_loss', 'before_backward', 'before_step',
         'after_step', 'after_cancel_batch', 'after_batch','End Batch Loop','End Train',
         'after_cancel_train', 'after_train', 'Start Valid', 'before_validate','Start Batch Loop',
         '**CBs same as train batch**', 'End Batch Loop', 'End Valid', 'after_cancel_validate',
         'after_validate', 'End Epoch Loop', 'after_cancel_epoch', 'after_epoch', 'End Fit',
         'after_cancel_fit', 'after_fit']

class Loop(GetAttr):
    _loop,_default,_events=_loop,'_base',None
    def __init__(self,cbs=None,**kwargs):
        store_attr(but='cbs')
        self.cbs=L()
        self.add_cbs(L(defaults.loop_callbacks)+L(cbs))
        self("after_create")

    def _grab_cbs(self, cb_cls): return L(cb for cb in self.cbs if isinstance(cb, cb_cls))

    def add_cbs(self, cbs):
        L(cbs).map(self.add_cb)
        return self

    def remove_cbs(self, cbs):
        L(cbs).map(self.remove_cb)
        return self

    def add_cb(self, cb):
        if isinstance(cb, type): cb = cb()
        setattr(cb,self._default,self)
        setattr(self, cb.name, cb)
        self.cbs.append(cb)
        return self

    def remove_cb(self, cb):
        if isinstance(cb, type): self.remove_cbs(self._grab_cbs(cb))
        else:
            setattr(cb,self._default,None)
            if hasattr(self, cb.name): delattr(self, cb.name)
            if cb in self.cbs: self.cbs.remove(cb)
        return self

    def _with_events(self, f, event_type, ex, final=noop):
        try: self(f'before_{event_type}');  f()
        except ex: self(f'after_cancel_{event_type}')
        self(f'after_{event_type}');  final()

    @contextmanager
    def added_cbs(self, cbs):
        self.add_cbs(cbs)
        try: yield
        finally: self.remove_cbs(cbs)

    @contextmanager
    def removed_cbs(self, cbs):
        self.remove_cbs(cbs)
        try: yield self
        finally: self.add_cbs(cbs)

    def ordered_cbs(self, event): return [cb for cb in self.cbs.sorted('order') if hasattr(cb, event)]
    def __call__(self, event_name): L(event_name).map(self._call_one)

    def _call_one(self, event_name):
        if not hasattr(self._events, event_name): raise Exception(f'missing {event_name}')
        for cb in self.cbs.sorted('order'): cb(event_name)


    def show_loop(self):
        indent = 0
        for s in self._loop:
            if s.startswith('Start'): print(f'{" "*indent}{s}'); indent += 2
            elif s.startswith('End'): indent -= 2; print(f'{" "*indent}{s}')
            else: print(f'{" "*indent} - {s:15}:', self.ordered_cbs(s))

# Cell
_events = L.split('')

mk_class('loop_event', **_events.map_dict(),
         doc="All possible events as attributes to get tab-completion and typo-proofing")

#nbdev_comment _all_ = ['loop_event']

# Cell
_inner_loop = "".split()

# Cell
@funcs_kwargs(as_method=True)
class LoopCallback(Stateful,GetAttr):
    "Basic class handling tweaks of a callback loop by changing a `obj` in various events"
    order,_default,obj,run,run_train,run_valid = 0,'obj',None,True,True,True
    end_event='after_fit'
    _methods = _events

    def __init__(self, **kwargs): assert not kwargs, f'Passed unknown events: {kwargs}'
    def __repr__(self): return type(self).__name__

    def __call__(self, event_name,**kwargs):
        "Call `self.{event_name}` if it's defined"
        _run = (event_name not in _inner_loop or (self.run_train and getattr(self, 'training', True)) or
               (self.run_valid and not getattr(self, 'training', False)))
        res=None
        if self.run and _run:
            res=getattr(self, event_name, noop)(**kwargs)
        if event_name==self.end_event: self.run=True #Reset self.run to True at each end of fit
        return res

    def __setattr__(self, name, value):
        if hasattr(self.obj,name):
            warn(f"You are shadowing an attribute ({name}) that exists in the {self._default}. Use `self.{self._default}.{name}` to avoid this")
        super().__setattr__(name, value)

    @property
    def name(self):
        "Name of the `LoopCallback`, camel-cased and with '*LoopCallback*' removed"
        return class2attr(self, 'LoopCallback')