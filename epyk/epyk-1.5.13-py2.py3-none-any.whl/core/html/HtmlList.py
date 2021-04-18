#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
List of all the different templates configurations available for displaying bespoke lists.
This list can be extended and it is easy to test a new configuration by different defining the HTML template in the
common list object.
List are standard and very popular HTML objects, please have a look at the below websites if you need further
information to manipulate them in your report

"""

from epyk.core.js import Imports
from epyk.core.js import JsUtils
from epyk.core.js.packages import JsQuery
from epyk.core.html import Html
from epyk.core.html.options import OptList

# The list of Javascript classes
from epyk.core.js.html import JsHtml
from epyk.core.js.html import JsHtmlList

from epyk.core.css.styles import GrpClsList


class Li(Html.Html):
  name = 'Entries'

  def __init__(self, report, text):
    super(Li, self).__init__(report, text)
    if hasattr(text, 'options'):
      text.options.managed = False
    self.css({'font-size': 'inherit', 'margin': "1px 5px", 'padding': 0})

  def __add__(self, component):
    """ Add items to a container """
    if not hasattr(component, 'options'):
      raise Exception("This can only be used for HTML components")

    self.set_html_content(component)
    return self

  def no_decoration(self):
    """
    Description:
    ------------
    Remove the list default style.

    Usage:
    -----

    """
    self.css({"text-decoration": "none", "list-style-type": 'none'})
    return self

  def add_label(self, text, css=None, position="before", for_=None, html_code=None, options=None):
    """
    Description:
    ------------
    Add an elementary label component.

    Usage:
    -----

    Related Pages:

      https://www.w3schools.com/tags/tag_label.asp

    Attributes:
    ----------
    :param text: String. The label content.
    :param css: Dictionary. Optional. A dictionary with the CSS style to be added to the component.
    :param position: String. Optional. The position.
    :param for_: Specifies which form element a label is bound to
    :param html_code: String. Optional. An identifier for this component (on both Python and Javascript side).
    :param options: Dictionary. Optional. Specific Python options available for this component.
    """
    self.label = ""
    if text is not None:
      dfl_css = {"float": 'none', 'width': 'none'}
      if css is not None:
        dfl_css.update(css)
      html_code_label = "%s_label" % html_code if html_code is not None else html_code
      self.label = self._report.ui.texts.label(text, options=options, html_code=html_code_label)
      if for_ is not None:
        # Attach the label to another HTML component based on the ID
        self.label.attr['for'] = for_
      if position == "before":
        self.prepend_child(self.label)
      else:
        self.append_child(self.label)
      self.label.css(dfl_css)
    return self

  def set_html_content(self, component):
    """
    Description:
    ------------
    Set the cell content to be an HTML object.

    Usage:
    -----

    Attributes:
    ----------
    :param component: HTML. Python HTML object.

    :return: self, the cell object to allow the chaining
    """
    component.options.managed = False
    if self.innerPyHTML is not None:
      if not isinstance(self.innerPyHTML, list):
        self.innerPyHTML = [self.innerPyHTML]
      self.innerPyHTML.append(component)
    else:
      self.innerPyHTML = component
    return self

  def click(self, js_funcs, profile=None, source_event=None, on_ready=False):
    """
    Description:
    ------------

    Usage:
    -----

    Attributes:
    ----------
    :param js_funcs: List | String. Javascript functions.
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage.
    :param source_event: String. Optional. The source target for the event.
    :param on_ready: Boolean. Optional. Specify if the event needs to be trigger when the page is loaded.
    """
    if self.innerPyHTML is not None:
      return self.innerPyHTML.click(js_funcs, profile)

    return super(Li, self).click(js_funcs, profile, source_event, on_ready=on_ready)

  def __str__(self):
    return "<li %s>%s</li>" % (self.get_attrs(pyClassNames=self.style.get_classes()), self.content)


class List(Html.Html):
  name = 'List'
  _option_cls = OptList.OptionsLi

  def __init__(self, report, data, color, width, height, html_code, helper, options, profile):
    super(List, self).__init__(report, [], css_attrs={"width": width, "height": height},
                               html_code=html_code, profile=profile, options=options)
    self.add_helper(helper)
    self.color = color if color is not None else self._report.theme.greys[-1]
    self.css({'padding': 0, 'margin': "1px", 'list-style-position': 'inside'})
    self.items = None
    for item in data:
      self.add_item(item)
    if len(data) > 0:
      self.set_items()

  @property
  def options(self):
    """
    Description:
    ------------
    Property to the component options.
    Options can either impact the Python side or the Javascript builder.

    Python can pass some options to the JavaScript layer.

    Usage:
    -----

    :rtype: OptList.OptionsLi
    """
    return super().options

  @property
  def dom(self):
    """
    Description:
    ------------
    Return all the Javascript functions defined for an HTML Component.
    Those functions will use plain javascript by default.

    Usage:
    -----

    :rtype: JsHtml.JsHtmlList
    """
    if self._dom is None:
      self._dom = JsHtml.JsHtmlList(self, report=self._report)
    return self._dom

  def items_style(self, style):
    """
    Description:
    ------------
    Function to load a predefined style for the items of the components.

    Usage:
    -----

    Attributes:
    ----------
    :param style. String. Mandatory. The alias of the style to apply.
    """
    if style == "bullets":
      bullter_style = {"display": 'inline-block', 'padding': '0 5px', 'margin-right': '2px',
                       'background': self._report.theme.greys[2],
                       'border': '1px solid %s' % self._report.theme.greys[2], 'border-radius': '10px'}
      self.options.li_css = bullter_style
      self.set_items()
      for item in self.items:
        item.css(self.options.li_css)
    return self

  def drop(self, js_funcs=None, prevent_default=True, profile=None):
    """
    Description:
    ------------

    Usage:
    -----

    Attributes:
    ----------
    :param js_funcs: List | String. Javascript functions.
    :param prevent_default: Boolean. Optional. Cancels the event if it is cancelable, meaning that the default action that belongs to the event will not occur.
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage.
    """
    from epyk.core.js.primitives import JsObjects

    if js_funcs is None:
      js_funcs = ["var wrapper = document.createElement('div'); wrapper.innerHTML = data",
        self.dom.add(JsObjects.JsObjects.get("(function(){if(typeof  wrapper.firstChild.innerText === 'undefined'){return wrapper.innerHTML} else{ return wrapper.firstChild.innerText}})()"))]
    else:
      if not isinstance(js_funcs, list):
        js_funcs = [js_funcs]
      js_funcs = ["var wrapper = document.createElement('div'); wrapper.innerHTML = data",
        self.dom.add(JsObjects.JsObjects.get("(function(){if(typeof  wrapper.firstChild.innerText === 'undefined'){return wrapper.innerHTML} else{ return wrapper.firstChild.innerText}})()"))] + js_funcs
    return super(List, self).drop(js_funcs, prevent_default, profile)

  def __add__(self, component):
    """ Add items to a container """
    if not isinstance(component, Li):
      raise Exception("This can only be used for Li")

    self.items = self.items or []
    component.options.managed = False
    self.items.append(component)
    return self

  def __getitem__(self, i):
    """
    Description:
    ------------
    Python function to get the elements of the lists which will be passed to the JavaScript.

    Usage:
    -----

    Attributes:
    ----------
    :param i: Integer. Get an element from the Python list.

    :rtype: Li
    """
    return self.items[i] if self.items is not None else None

  def add_item(self, d):
    """
    Description:
    ------------
    Add an element to the list before passing the list to the Javascript.

    Usage:
    -----

    Attributes:
    ----------
    :param d: HTML component | String. The component to be added.
    """
    self.items = self.items or []
    li_obj = Li(self._report, d)
    if hasattr(d, 'options'):
      d.options.managed = False
    li_obj.options.managed = False
    self.items.append(li_obj)
    return self

  def set_items(self):
    """
    Description:
    ------------
    Reset all the items in the list by applying the default styles,

    Usage:
    -----

    """
    self.items = self.items or []
    for d in self.val:
      li_obj = Li(self._report, d)
      li_obj.options.managed = False
      li_obj.css(self.options.li_css)
      if self.options.li_class:
        li_obj.attr["class"].add(self.options.li_class)
      self.items.append(li_obj)
    return self

  def on_items(self, event, js_funcs, profile=None):
    """
    Description:
    ------------
    Add event to the list items.

    Usage:
    -----

    Attributes:
    ----------
    :param event: String. The event type.
    :param js_funcs: List | String. Javascript functions.
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage.
    """
    for i in self.items:
      i.on(event, js_funcs, profile)
    return self

  def click_items(self, js_funcs, profile=None):
    """
    Description:
    ------------
    Add click events on the list items.

    Usage:
    -----

    Attributes:
    ----------
    :param js_funcs: List | String. Javascript functions.
    :param profile: Boolean or Dictionary. Optional. A flag to set the component performance storage.
    """
    js_funcs = JsUtils.jsConvertFncs(js_funcs)
    for i, item in enumerate(self.items):
      fnc = JsUtils.jsConvertFncs([
        self._report.js.getElementsByName("divs_%s" % self.htmlCode).all(self._report.js.objects.dom("elt").hide().r),
        self._report.js.getElementsByName("divs_%s" % self.htmlCode)[i].toggle().r])
      item.click(fnc + js_funcs, profile)
    return self

  def __str__(self):
    self._vals = "".join([i.html() for i in self.items]) if self.items is not None else ""
    return "<ul %s>%s</ul>" % (self.get_attrs(pyClassNames=self.style.get_classes()), self._vals)


class Groups(Html.Html):
  name = 'Groups'

  def __init__(self, report, data, categories, size, color, width, height, html_code, helper, options, profile):
    super(Groups, self).__init__(report, [], css_attrs={"width": width, "height": height}, options=options,
                                 html_code=html_code, profile=profile)
    self.add_helper(helper)
    self.color = color if color is not None else self._report.theme.greys[9]
    self.css({'font-size': "%s%s" % (size[0], size[1]) if size is not None else 'inherit',
              'margin': "1px", 'padding': '0 2px'})
    self.builder_name, self._lists__map, self._lists__map_index = False, {}, []
    for i, cat in enumerate(categories):
      self.add_list(data[i], cat)

  def __getitem__(self, i):
    return self.val[i]

  def add_list(self, data, category="", color='inherit', width=(None, 'px'), height=(None, 'px'),
               html_code=None, helper=None, options=None, profile=None):
    """
    Description:
    ------------

    Usage:
    -----

    Attributes:
    ----------
    :param data:
    :param category:
    :param color:
    :param width:
    :param height:
    :param html_code:
    :param helper:
    :param options:
    :param profile:
    """
    self._lists__map[category] = len(self.val)
    html_li = List(self._report, data, color, width, height, html_code, helper, options, profile)
    html_li.options.managed = False
    html_li.css({"margin-bottom": '5px'})
    self.val.append(html_li)
    self._lists__map_index.append(category)
    return self

  def __str__(self):
    self._vals = "".join(['''
      <a onclick='this.nextElementSibling.querySelectorAll("li").forEach(
        function(evt){evt.style.display = evt.style.display === "none" ? "" : "none"})' style='cursor:pointer'>%s</a>%s
      ''' % (
      self._lists__map_index[i] if len(self._lists__map_index) > i else "Category %s" % i,
      l.html()) for i, l in enumerate(self.val)])
    self.builder_name = self.__class__.__name__
    return "<div %s>%s</div>" % (self.get_attrs(pyClassNames=self.style.get_classes()), self._vals)


class Items(Html.Html):
  name = 'List'
  _option_cls = OptList.OptionsItems

  def __init__(self, report, records, width, height, options, html_code, profile, helper):
    super(Items, self).__init__(report, records, html_code=html_code, profile=profile, options=options,
                                css_attrs={"width": width, 'height': height})
    self.add_helper(helper, css={"float": "none", "margin-left": "5px"})

  @property
  def style(self):
    """
    Description:
    -----------
    Property to the CSS Style of the component.

    Usage:
    -----

    :rtype: GrpClsList.ClassItems
    """
    if self._styleObj is None:
      self._styleObj = GrpClsList.ClassItems(self)
    return self._styleObj

  def record(self, values):
    """
    Description:
    -----------
    A function helper to set values from Python in this object.

    Attributes:
    ----------
    :param values: Dict | List. The items to be added to the list.
    """
    records = []
    if isinstance(values, dict):
      for k, v in values.items():
        records.append({"text": k, "tooltip": v})
    else:
      records = values
    self._vals = records

  _js__builder__ = ''' htmlObj.innerHTML = "";
      data.forEach(function(item, i){
        if(options.showdown){var converter = new showdown.Converter(options.showdown); 
          converter.setOption("display", "inline-block"); var content = item; 
          if(typeof item.content !== 'undefined'){content = item.content}
          else if(typeof item.text !== 'undefined'){content = item.text};
          var content = converter.makeHtml(content).replace("<p>", "<p style='display:inline-block;margin:0'>")};
        var li = document.createElement("li");
        Object.keys(options.li_style).forEach(function(key){li.style[key] = options.li_style[key]});
        if(typeof item.type === 'undefined'){window[options.prefix+ options.items_type](li, item, options)}
        else{window[options.prefix + item.type](li, item, options)};
        if(typeof item.tooltip !== 'undefined'){
          var info = document.createElement("i");
          info.classList.add(...options.info_icon.split(" ")); info.style.position = 'absolute';
          info.style.top = "5px"; info.style.right = "20px";
          li.style.position = "relative";
          
          info.setAttribute('title', item.tooltip); 
          info.setAttribute('data-html', true); 
          info.setAttribute('data-placement', 'right'); 
          info.setAttribute('data-toggle', 'tooltip'); 
          li.lastChild.style.display = 'inline-block'; li.appendChild(info);
          %s.tooltip();
          
        }
        if(options.delete){
          var close = document.createElement("i");
          close.classList.add(...options.delete_icon.split(" ")); close.style.position = 'absolute';
          close.style.right = "0"; close.style.cursor = 'pointer';
          close.onclick = function(event){this.parentNode.remove()};
          li.style.position = "relative";
          for (const [key, value] of Object.entries(options.delete_position)){
            close.style[key] = value}
          li.lastChild.style.display = 'inline-block'; li.appendChild(close)}
        if(options.items_space){li.style.margin = "5px 0"; li.style.padding = "2px 0"}
        htmlObj.appendChild(li)})''' % JsQuery.decorate_var("info", convert_var=False)

  @property
  def options(self):
    """
    Description:
    ------------
    Property to the component options.
    Options can either impact the Python side or the Javascript builder.

    Python can pass some options to the JavaScript layer.

    Usage:
    -----

    :rtype: OptList.OptionsItems
    """
    return super().options

  @property
  def dom(self):
    """
    Description:
    ------------
    Return all the Javascript functions defined for an HTML Component.
    Those functions will use plain javascript by default.

    Usage:
    -----

    :rtype: JsHtmlList.JsItem
    """
    if self._dom is None:
      self._dom = JsHtmlList.JsItem(self, report=self._report)
    return self._dom

  def click(self, js_funcs, profile=None, source_event=None, on_ready=False):
    """
    Description:
    ------------
    The onclick event occurs when the user clicks on an element of the list.

    Usage:
    -----

    Attributes:
    ----------
    :param js_funcs: List | String. Javascript functions.
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage.
    :param source_event: String. Optional. The source target for the event.
    :param on_ready: Boolean. Optional. Specify if the event needs to be trigger when the page is loaded.
    """
    if not isinstance(js_funcs, list):
      js_funcs = []
    self.options.click = "function(event, value){%s} " % JsUtils.jsConvertFncs(js_funcs, toStr=True, profile=profile)
    return self

  def draggable(self, js_funcs=None, options=None, profile=None, source_event=None):
    """
    Description:
    ------------

    Usage:
    -----

    Attributes:
    ----------
    :param js_funcs: List | String. Optional. Javascript functions.
    :param options: Dictionary. Optional. Specific Python options available for this component.
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage.
    :param source_event: String. Optional. The source target for the event.
    """
    js_funcs = js_funcs or []
    if not isinstance(js_funcs, list):
      js_funcs = [js_funcs]
    js_funcs.append('event.dataTransfer.setData("text", value)')
    self.options.draggable = "function(event, value){%s} " % JsUtils.jsConvertFncs(
      js_funcs, toStr=True, profile=profile)
    return self

  def add_type(self, name, item_def, dependencies=None):
    """
    Description:
    ------------
    Add a bespoke item type with it is specific style and components.

    TODO: Create a tutorial to explain how to extend list types.

    Usage:
    -----

    Attributes:
    ----------
    :param name: String. The reference of this type name in the framework.
    :param item_def: String. The definition of the items (examples in JsHtmlList.py).
    :param dependencies: List. Optional. The external module dependencies.
    """
    if dependencies is not None:
      for d in dependencies:
        if d in Imports.JS_IMPORTS:
          self._report.jsImports.add(d)
        if d in Imports.CSS_IMPORTS:
          self._report.cssImport.add(d)
    self.style.css.padding_left = 0
    self.css({"list-style": 'none'})
    self.options.items_type = name
    item_type_name = "%s%s" % (self.options.prefix, self.options.items_type)
    self.page.properties.js.add_constructor(item_type_name, "function %s(htmlObj, data, options){%s}" % (
      item_type_name, JsHtmlList.JsItemsDef(self).custom(item_def)))
    return self

  def select_type(self, name=None, style=None, selected_style=None):
    """
    Description:
    ------------
    Set the CSS Style of the items in the list.
    It is possible to use predefined style or to pass bespoke ones.

    Style will be set at list type level so all the list in the page will be using it.

    Usage:
    -----

    Attributes:
    ----------
    :param name: String. Optional. The list type name to be used.
    :param style: Dictionary. Optional. The CSS style to be applied to the item.
    :param selected_style: Dictionary. Optional. The css style to be applied when selected.
    """
    li_attrs = self.options.style
    if style is None:
      li_attrs["padding"] = "2px 5px"
    else:
      li_attrs.update(style)
    self.options.style = li_attrs
    self.style.add_custom_class(selected_style or self.style.defined.selected_text_background_color(),
                                classname="list_%s_selected" % (name or self.options.items_type))

  def __str__(self):
    item_type_name = "%s%s" % (self.options.prefix, self.options.items_type)
    self.options.style_select = "list_%s_selected" % self.options.items_type
    # add all the shape definitions
    if not self.page.properties.js.has_constructor(item_type_name):
      shapes = JsHtmlList.JsItemsDef(self)
      self.page.properties.js.add_constructor(item_type_name, "function %s(htmlObj, data, options){%s}" % (
        item_type_name, getattr(shapes, self.options.items_type)(self._report)))
    self.page.properties.js.add_builders(self.refresh())
    return '<ul %s></ul>%s' % (self.get_attrs(pyClassNames=self.style.get_classes()), self.helper)


class ListTournaments(Html.Html):
  name = 'Brackets'
  requirements = ('jquery-bracket', )
  _option_cls = OptList.OptionsListBrackets

  def __init__(self, report, records, width, height, options, profile):
    super(ListTournaments, self).__init__(
      report, records, options=options, profile=profile, css_attrs={"width": width, "height": height})
    self.css({'overflow': 'auto', "padding": "auto", "margin": "auto"})

  _js__builder__ = '''options.init = data; %(jqId)s.bracket(options)
      ''' % {"jqId": JsQuery.decorate_var("htmlObj", convert_var=False)}

  def __str__(self):
    self.page.properties.js.add_builders(self.refresh())
    return "<div %s></div>" % self.get_attrs(pyClassNames=self.style.get_classes())
