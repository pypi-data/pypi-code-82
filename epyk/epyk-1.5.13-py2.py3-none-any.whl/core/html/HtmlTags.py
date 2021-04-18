#!/usr/bin/python
# -*- coding: utf-8 -*-


from epyk.core.html.options import OptText

from epyk.core.html import Html
from epyk.core.js.html import JsHtml


class HtmlGeneric(Html.Html):
  name = 'tag'
  _option_cls = OptText.OptionsText

  def __init__(self, report, tag, text, width, height, html_code, tooltip, options, profile):
    self.tag = tag
    super(HtmlGeneric, self).__init__(report, text, html_code=html_code, css_attrs={"width": width, "height": height},
                                      options=options, profile=profile)
    if tooltip:
      self.tooltip(tooltip)
    if options is not None and not options.get('managed', True):
      self.options.managed = False

  @property
  def options(self):
    """
    Description:
    ------------
    Property to set all the possible object for a button.

    Usage:
    -----

    :rtype: OptText.OptionsText
    """
    return super().options

  def __getitem__(self, i):
    if not isinstance(self.val, list):
      return self.val

    return self.val[i]

  def __add__(self, component):
    """ Add items to a container """
    # Has to be defined here otherwise it is set to late
    component.options.managed = False
    if not isinstance(self.val, list):
      self._vals = [] if self.val is None else [self.val]
    if component is not None:
      self.val.append(component)
    return self

  @property
  def dom(self):
    """
    Description:
    ------------
    Return all the Javascript functions defined for an HTML Component.
    Those functions will use plain javascript by default.

    Usage:
    -----

    :return: A Javascript Dom object

    :rtype: JsHtml.JsHtmlRich
    """
    if self._dom is None:
      self._dom = JsHtml.JsHtmlRich(self, report=self._report)
    return self._dom

  _js__builder__ = 'htmlObj.innerHTML = data'

  def __str__(self):
    if isinstance(self.val, list):
      str_val = "".join([v.html() if hasattr(v, 'html') else v for v in self.val])
      return '<%s %s>%s</%s>%s' % (self.tag, self.get_attrs(pyClassNames=self.style.get_classes()), str_val,
                                   self.tag, self.helper)

    return '<%s %s>%s</%s>%s' % (self.tag, self.get_attrs(pyClassNames=self.style.get_classes()), self.val,
                                 self.tag, self.helper)


class HtmlGenericLInk(HtmlGeneric):
  name = 'tag'

  def preview(self, url, profile=None):
    """
    Description:
    ------------

    Usage:
    -----

    Attributes:
    ----------
    :param url: String. The url path.
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage.
    """
    self.on('mouseenter', [
      self._report.js.request_http("test", 'GET', url).send().onSuccess([
        self._report.js.createElement("div", "popup").innerHTML(
          self._report.js.object("data")).attr('id', 'popup').css(
          {'color': 'red', 'display': 'block', 'background': 'white', 'width': '250px', 'padding': '10px'}).position(),
        self._report.body.dom.appendChild(self._report.js.object("popup"))]
      )
    ], profile=profile)

    self.on('mouseleave', [self._report.js.getElementById("popup").remove()], profile=profile)


class HtmlComment(Html.Html):
  name = 'comment'

  def __str__(self):
    return '<!--%s-->' % self.val
