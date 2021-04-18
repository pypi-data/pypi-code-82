
import sys

from epyk.core.css import Properties
from epyk.core.css import Defaults_css


class Attrs(Properties.CssMixin):

  def __init__(self, component):
    self.attrs = {}
    self.component = component
    self._report = component.page
    self.page = component.page

  def css(self, attrs, value=None, important=False):
    """
    Description:
    ------------
    Set multiple CSS attributes to the HTML component.

    Attributes:
    ----------
    :param attrs: Dictionary | String. optional. The attributes to be added.
    :param value: String. Optional. The value for a given item.
    :param important: Boolean. Optional. Flag the attribute to be important.
    """
    if not isinstance(attrs, dict):
      if value is None:
        return self.attrs.get(attrs)

      if important:
        value = "%s !IMPORTANT" % value
      self.attrs[attrs] = value

    for k, v in attrs.items():
      if important:
        v = "%s !IMPORTANT" % v
      self.attrs[k] = v
    return self.attrs

  def remove(self, attr=None, set_none=False):
    """
    Description:
    ------------
    Remove a CSS attribute to the HTML component.

    This function will either remove it if it is part of the existing CSS attribute or set it to auto in case it is
    coming from a CSS class.

    Attributes:
    ----------
    :param attr: String. Optional. The attribute to be removed.
    :param set_none: Boolean. Optional. Set the CSS attribute value to None on the CSS.
    """
    key = attr or sys._getframe().f_back.f_code.co_name.replace("_", "-")
    if set_none:
      self.attrs[key] = "none"
      self.component.attr['css'][key] = "none"
    else:
      if key in self.attrs:
        del self.attrs[key]
        if key in self.component.attr['css']:
          del self.component.attr['css'][key]
      else:
        self.attrs[key] = "unset"
        self.component.attr['css'][key] = "auto"

  def __str__(self):
    css_tag = ["%s:%s" % (k, v) for k, v in self.attrs.items()]
    return ";".join(css_tag)


class Commons(Attrs):

  def __init__(self, component):
    super(Commons, self).__init__(component)
    self.font_size = 'inherit'
    self.font_family = 'inherit'
    self.box_sizing = 'border-box'


class Empty(Attrs):

  def __init__(self, component):
    super(Empty, self).__init__(component)


class Body(Attrs):

  def __init__(self, component):
    super(Body, self).__init__(component)
    self.font_size = component.style.globals.font.normal()
    self.font_family = component.style.globals.font.family
    self.margin = 0
