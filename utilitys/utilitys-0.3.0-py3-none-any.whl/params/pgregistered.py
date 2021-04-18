from __future__ import annotations

import warnings
from pathlib import Path
from typing import Optional

import numpy as np
from pyqtgraph.Qt import QtGui, QtWidgets, QtCore
from pyqtgraph.parametertree import parameterTypes, Parameter
from pyqtgraph.parametertree.Parameter import PARAM_TYPES
from pyqtgraph.parametertree.parameterTypes import ActionParameterItem, ActionParameter, \
  TextParameterItem, TextParameter

from .prjparam import PrjParam
from .shortcut import ShortcutsEditor
from ..fns import clsNameOrGroup, params_flattened, popupFilePicker
from ..widgets import PopupLineEditor, ButtonCollection


class MonkeyPatchedTextParameterItem(TextParameterItem):
  def makeWidget(self):
    textBox: QtWidgets.QTextEdit = super().makeWidget()
    textBox.setTabChangesFocus(True)
    return textBox

# Monkey patch pyqtgraph text box to allow tab changing focus
TextParameter.itemClass = MonkeyPatchedTextParameterItem

class PgParamDelegate(QtWidgets.QStyledItemDelegate):
  def __init__(self, paramDict: dict, parent=None):
    super().__init__(parent)
    errMsg = f'{self.__class__} can only create parameter editors from' ' registered pg widgets that implement ' \
             f'makeWidget() and are in pyqtgraph\'s *PARAM_TYPES*.\n' \
             f'Cannot find {self.__class__}'

    if paramDict['type'] not in PARAM_TYPES:
      raise TypeError(errMsg)
    paramDict.update(name='dummy')
    self.param = param = Parameter.create(**paramDict)
    if hasattr(param.itemClass, 'makeWidget'):
      self.item = param.itemClass(param, 0)
    else:
      raise TypeError(errMsg)

  def createEditor(self, parent, option, index: QtCore.QModelIndex):
    # TODO: Deal with params that go out of scope before yielding a value
    editor = self.item.makeWidget()
    editor.setParent(parent)
    editor.setMaximumSize(option.rect.width(), option.rect.height())
    return editor

  def setModelData(self, editor: QtWidgets.QWidget,
                   model: QtCore.QAbstractTableModel,
                   index: QtCore.QModelIndex):
    model.setData(index, editor.value())

  def setEditorData(self, editor: QtWidgets.QWidget, index):
    value = index.data(QtCore.Qt.EditRole)
    editor.setValue(value)

  def updateEditorGeometry(self, editor: QtWidgets.QWidget,
                           option: QtWidgets.QStyleOptionViewItem,
                           index: QtCore.QModelIndex):
    editor.setGeometry(option.rect)

class KeySequenceParameterItem(parameterTypes.WidgetParameterItem):
  """
  Class for creating custom shortcuts. Must be made here since pyqtgraph doesn't
  provide an implementation.
  """

  def makeWidget(self):
    item = QtWidgets.QKeySequenceEdit()

    item.sigChanged = item.editingFinished
    item.value = lambda: item.keySequence().toString()
    def setter(val: QtGui.QKeySequence):
      if val is None or len(val) == 0:
        item.clear()
      else:
        item.setKeySequence(val)
    item.setValue = setter
    self.param.seqEdit = item

    return item

  def updateDisplayLabel(self, value=None):
    # Make sure the key sequence is human readable
    self.displayLabel.setText(self.widget.keySequence().toString())

  # def contextMenuEvent(self, ev: QtGui.QContextMenuEvent):
  #   menu = self.contextMenu
  #   delAct = QtWidgets.QAction('Set Blank')
  #   delAct.triggered.connect(lambda: self.widget.setValue(''))
  #   menu.addAction(delAct)
  #   menu.exec(ev.globalPos())

class _Global: pass

class KeySequenceParameter(Parameter):
  itemClass = KeySequenceParameterItem

class ShortcutParameterItem(ActionParameterItem):

  def __init__(self, param, depth):
    # Force set title since this will get nullified on changing the button parent for some
    # reason
    super().__init__(param, depth)
    btn: QtWidgets.QPushButton = self.button
    self.setText(0, '')
    owner = param.opts.get('ownerObj', _Global)
    # Add things like icon and help text
    prjOpts = PrjParam(**param.opts)
    ButtonCollection.createBtn(prjOpts, baseBtn=self.button, namePath=(clsNameOrGroup(owner),))

  def _postInit_(self, shcParam: Parameter):
    """
    Exists purely to assist shortcutWithKeySeq in grabbing the created shortcut parameter and placing it next to
    the button instead of in the shortcuts editor
    """
    pass


class ShortcutParameter(ActionParameter):
  itemClass = ShortcutParameterItem
  REGISTRY: Optional[ShortcutsEditor]=None

  @classmethod
  def setRegistry(cls, shortcutsRegistry: ShortcutsEditor=None, createIfNone=False, **createOpts):
    if cls.REGISTRY:
      with warnings.catch_warnings():
        warnings.simplefilter('ignore', UserWarning)
        for param in params_flattened(cls.REGISTRY.params):
          cls.REGISTRY.deleteShortcut(PrjParam(param.name(), param.defaultValue()))
    if createIfNone and shortcutsRegistry is None:
      shortcutsRegistry = ShortcutsEditor(**createOpts)
    cls.REGISTRY = shortcutsRegistry
    return shortcutsRegistry

class ShortcutKeySeqParameterItem(ShortcutParameterItem):

  def _postInit_(self, shcParam: Parameter):
    shcParam.remove()
    self.keySeqEdit: KeySequenceParameterItem = shcParam.makeTreeItem(self.depth)

    # Make sure that when a parameter is removed, the shortcut is also deactivated. Since the key sequence was stolen
    # from the shortcut editor, it must be addressed here
    def onRemove():
      shcParam.setValue('')
      shcParam.remove()
    self.param.sigRemoved.connect(lambda: onRemove())
    self.layout.addWidget(self.keySeqEdit.widget)

class ShortcutKeySeqParameter(ActionParameter):
  itemClass = ShortcutKeySeqParameterItem

  def __init__(self, **opts):
    # TODO: Find way to get shortcuts working well with general shortcut editor.
    #  for now, just make sure no shortcuts are registered
    opts.pop('value', None)
    super().__init__(**opts)
    self.isActivateConnected = False


class PopupLineEditorParameterItem(parameterTypes.WidgetParameterItem):
  def __init__(self, param, depth):
    strings = param.opts.get('limits', [])
    self.model = QtCore.QStringListModel(strings)
    param.sigLimitsChanged.connect(
      lambda _param, limits: self.model.setStringList(limits)
    )
    super().__init__(param, depth)

  def makeWidget(self):
    editor = PopupLineEditor(model=self.model, clearOnComplete=False)
    editor.setValue = editor.setText
    editor.value = editor.text
    editor.sigChanged = editor.editingFinished
    return editor

  def widgetEventFilter(self, obj, ev):
    # Prevent tab from leaving widget
    return False

class PopupLineEditorParameter(Parameter):
  itemClass = PopupLineEditorParameterItem

class ProcGroupParameterItem(parameterTypes.GroupParameterItem):

  def __init__(self, param, depth):
    self.enabledFontMap = None
    super().__init__(param, depth)

  def _mkFontMap(self):
    if self.enabledFontMap:
      return
    allowDisable = self.param.opts['process'].allowDisable
    if allowDisable:
      enabledFont = self.font(0)
    else:
      enabledFont = QtGui.QFont()
      enabledFont.setBold(False)

    disableFont = QtGui.QFont()
    disableFont.setStrikeOut(True)
    self.enabledFontMap = {True: enabledFont, False: disableFont}


  def optsChanged(self, param, opts):
    proc = param.opts['process']
    if 'enabled' in opts:
      enabled = opts['enabled']
      if proc.allowDisable:
        # Bypass subclass to prevent early short-circuit
        if enabled:
          super().setData(0, QtCore.Qt.CheckStateRole, QtCore.Qt.Checked)
        else:
          super().setData(0, QtCore.Qt.CheckStateRole, QtCore.Qt.Unchecked)
      # This gets called before constructor can finish, so add enabled font map here
      proc.disabled = not enabled
      self._mkFontMap()
      self.setFont(0, self.enabledFontMap[enabled])

  def updateFlags(self):
    # It's a shame super() doesn't return flags...
    super().updateFlags()
    opts = self.param.opts
    flags = self.flags()
    if opts['process'].allowDisable:
      flags |= QtCore.Qt.ItemIsUserCheckable & (~QtCore.Qt.ItemIsTristate)
    self.setFlags(flags)

  def setData(self, column, role, value):
    isChk = role == QtCore.Qt.CheckStateRole
    # Check for invalid request to change check state
    if isChk and self.param.parent() and not self.param.parent().opts['enabled']:
      return
    checkstate = self.checkState(column)
    super().setData(column, role, value)
    if isChk and int(checkstate) != value:
      self.param.setOpts(enabled=bool(value))

class ProcGroupParameter(parameterTypes.GroupParameter):
  itemClass = ProcGroupParameterItem

  def setOpts(self, **opts):
    enabled = opts.get('enabled')
    curEnabled = self.opts['enabled']
    super().setOpts(**opts)
    if enabled is not None and enabled != curEnabled:
      for chParam in filter(lambda el: isinstance(el, ProcGroupParameter), self):
        chParam.setOpts(enabled=enabled)

class _DummySignal:
  def connect(self, *args): pass
  def disconnect(self, *args): pass

# WidgetParameterItem is not a QObject, so it can't emit signals. Use a dummy class instead
class _Emitter(QtCore.QObject):
  sigChanging = QtCore.Signal(object)
  sigChanged = QtCore.Signal(object)

class FilePickerParameterItem(parameterTypes.WidgetParameterItem):
  def makeWidget(self):
    param = self.param
    self._emitter = _Emitter()

    if param.opts['value'] is None:
      param.opts['value'] = ''
    fpath = param.opts['value']
    param.opts.setdefault('asFolder', False)
    param.opts.setdefault('existing', True)
    button = QtWidgets.QPushButton()
    button.setValue = button.setText
    button.sigChanged = self._emitter.sigChanged
    button.value = button.text
    button.setText(fpath)
    button.clicked.connect(self._retrieveFolderName_gui)

    return button

  def _retrieveFolderName_gui(self):
    curVal = self.param.value()
    useDir = curVal or str(Path.cwd())
    opts = self.param.opts
    opts['startDir'] = str(Path(useDir).absolute())
    fname = popupFilePicker(None, 'Select File', **opts)
    if fname is None:
      return
    self.param.setValue(fname)
    self._emitter.sigChanged.emit(fname)

class FilePickerParameter(Parameter):
  itemClass = FilePickerParameterItem

class SliderParameterItem(parameterTypes.WidgetParameterItem):
  slider: QtWidgets.QSlider
  span: np.ndarray
  charSpan: np.ndarray

  def makeWidget(self):
    param = self.param
    opts = param.opts
    # Bind to self to avoid garbage collection of signal holder
    # Bind to self to avoid garbage collection of signal holder
    _emitter = self._emitter = _Emitter()


    self.slider = QtWidgets.QSlider()
    self.slider.setOrientation(QtCore.Qt.Horizontal)
    lbl = QtWidgets.QLabel()
    lbl.setAlignment(QtCore.Qt.AlignLeft)

    w = QtWidgets.QWidget()
    layout = QtWidgets.QHBoxLayout()
    w.setLayout(layout)
    layout.addWidget(lbl)
    layout.addWidget(self.slider)

    def setValue(v):
      self.slider.setValue(self.spanToSliderValue(v))
    def getValue():
      return self.span[self.slider.value()].item()

    def vChanged(v):
      lbl.setText(self.prettyTextValue(v))
    self.slider.valueChanged.connect(vChanged)

    def onMove(pos):
      _emitter.sigChanging.emit(self.span[pos].item())
    self.slider.sliderMoved.connect(onMove)

    w.setValue = setValue
    w.value = getValue
    w.sigChanged = self.slider.valueChanged
    w.sigChanging = _emitter.sigChanging
    self.optsChanged(param, opts)
    return w

  # def updateDisplayLabel(self, value=None):
  #   self.displayLabel.setText(self.prettyTextValue(value))

  def spanToSliderValue(self, v):
    return int(np.argmin(np.abs(self.span-v)))

  def prettyTextValue(self, v):
    format_ = self.param.opts.get('format', None)
    cspan = self.charSpan
    if format_ is None:
      format_ = f'{{0:>{cspan.dtype.itemsize}}}'
    return format_.format(cspan[v].decode())

  def optsChanged(self, param, opts):
    try:
      super().optsChanged(param, opts)
    except AttributeError as ex:
      pass
    span = opts.get('span', None)
    if span is None:
      step = opts.get('step', 1)
      start, stop = opts['limits']
      # Add a bit to 'stop' since python slicing excludes the last value
      span = np.arange(start, stop+step, step)
    precision = opts.get('precision', 2)
    if precision is not None:
      span = span.round(precision)
    self.span = span
    self.charSpan = np.char.array(span)
    w = self.slider
    w.setMinimum(0)
    w.setMaximum(len(span)-1)

  def limitsChanged(self, param, limits):
    self.optsChanged(param, dict(limits=limits))

class SliderParameter(Parameter):
  itemClass = SliderParameterItem

class ChecklistParameter(parameterTypes.GroupParameter):

  def __init__(self, **opts):
    opts.setdefault('exclusive', False)
    # Value setting before init causes problems since limits aren't set by that point.
    # Avoid by taking value out of consideration until later
    value = opts.pop('value', None)
    super().__init__(**opts)
    self.setOpts(**opts)
    if value is not None:
      self.setValue(value)
    self.sigOptionsChanged.connect(lambda obj, opts: self.setOpts(**opts))

  def setLimits(self, limits):
    super().setLimits(limits)
    exclusive = self.opts['exclusive']
    oldOpts = {n: self[n] for n in self.names}
    self.clearChildren()
    for chOpts in limits:
      if isinstance(chOpts, str):
        newVal = oldOpts.get(chOpts, not exclusive)
        chOpts = dict(name=chOpts, value=newVal)
      child = self.create(type='bool', **chOpts)
      self._hookupParam(child, exclusive)
      self.addChild(child)
    if exclusive and len(self.value()) != 1:
      self.setValue(limits[-1])

  def _hookupParam(self, param, exclusive):
    def onChange_exclusive(_param, value):
      if value:
        self.setValue(param.name())
    def onChange_default(_param, value):
      self.sigValueChanged.emit(self, self.value())
    if exclusive:
      param.sigValueChanged.connect(onChange_exclusive)
    else:
      param.sigValueChanged.connect(onChange_default)

  def setOpts(self, **opts):
    if 'exclusive' in opts and 'limits' not in opts:
      self.setLimits(self.opts.get('limits', []))
    super().setOpts(**opts)

  def value(self):
    vals = [p.name() for p in self.children() if p.value()]
    if not vals or not self.opts['exclusive']:
      return vals
    return vals[0]

  def setValue(self, value, blockSignal=None):
    exclusive = self.opts['exclusive']
    # Will emit at the end, so no problem discarding existing changes
    if exclusive:
      value = [value]
    value = [v for v in value if v in self.names]
    if value == self.value():
      return value
    for chParam in self.childs:
      chParam.setValue(chParam.name() in value)
      if exclusive:
        chParam.setReadonly(chParam.value())
    newVal = self.value()
    self.sigValueChanged.emit(self, newVal)
    return newVal

class NoneParameter(parameterTypes.SimpleParameter):

  def __init__(self, **opts):
    opts['type'] = 'str'
    super().__init__(**opts)
    self.setWritable(False)

parameterTypes.registerParameterType('NoneType', NoneParameter)
parameterTypes.registerParameterType('keyseq', KeySequenceParameter)
parameterTypes.registerParameterType('procgroup', ProcGroupParameter)
parameterTypes.registerParameterType('shortcutkeyseq', ShortcutKeySeqParameter)
parameterTypes.registerParameterType('shortcut', ShortcutParameter)
parameterTypes.registerParameterType('popuplineeditor', PopupLineEditorParameter)
parameterTypes.registerParameterType('filepicker', FilePickerParameter)
parameterTypes.registerParameterType('slider', SliderParameter)
parameterTypes.registerParameterType('checklist', ChecklistParameter)
