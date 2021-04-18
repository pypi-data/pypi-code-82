#!/usr/bin/python
# -*- coding: utf-8 -*-

from epyk.core.html.options import Options
from epyk.core.js.packages import packageImport


class OptionsText(Options):

  @property
  def editable(self):
    """
    Description:
    ------------
    Set the content of the component editable.

    Related Pages:

      https://www.w3schools.com/tags/att_global_contenteditable.asp
    """
    return self._report.attr.get("contenteditable", False)

  @editable.setter
  def editable(self, flag):
    self.component.page.body.style.contenteditable()
    self.component.attr["contenteditable"] = flag
    if flag:
      self.spellcheck = False

  @property
  def spellcheck(self):
    """
    Description:
    ------------
    The spellcheck attribute specifies whether the element is to have its spelling and grammar checked or not.

    Related Pages:

      https://www.w3schools.com/tags/att_global_spellcheck.asp
    """
    return self._report.attr.get("spellcheck", False)

  @spellcheck.setter
  def spellcheck(self, flag):
    self.component.page.body.style.contenteditable()
    self.component.attr["spellcheck"] = flag

  @property
  def reset(self):
    """
    Description:
    ------------

    Related Pages:
    """
    return self._config_get(False)

  @reset.setter
  def reset(self, flag):
    self._config(flag)

  @property
  def markdown(self):
    """
    Description:
    ------------
    Showdown is a Javascript Markdown to HTML converter, based on the original works by John Gruber.
    Showdown can be used client side (in the browser) or server side (with NodeJs).

    Related Pages:

      https://github.com/showdownjs/showdown
    """
    return self._config_get(False)

  @markdown.setter
  @packageImport("showdown", if_true=True)
  def markdown(self, values):
    if isinstance(values, bool):
      self._config(values)
      self._config({} if values is True else values, 'showdown')
    else:
      self._config(True)
      self._config(values, 'showdown')

  @property
  def showdown(self):
    """
    Description:
    ------------
    Showdown is a Javascript Markdown to HTML converter, based on the original works by John Gruber.
    Showdown can be used client side (in the browser) or server side (with NodeJs).

    Related Pages:

      https://github.com/showdownjs/showdown
    """
    return self._config_get(False)

  @showdown.setter
  @packageImport("showdown")
  def showdown(self, values):
    self._config(True, 'markdown')
    self._config(values)

  @property
  def limit_char(self):
    """
    Description:
    ------------

    Related Pages:

    """
    return self._config_get(None, 'limit_char')

  @limit_char.setter
  def limit_char(self, value):
    self._config(value, "maxlength")

  @property
  def red(self):
    """
    Description:
    ------------

    Related Pages:

    """
    return self._config_get(self._report.theme.danger[1])

  @red.setter
  def red(self, value):
    self._config(value)

  @property
  def green(self):
    """
    Description:
    ------------

    Related Pages:

    """
    return self._config_get(self.component.page.theme.success[1])

  @green.setter
  def green(self, value):
    self._config(value)

  @property
  def orange(self):
    """
    Description:
    ------------

    Related Pages:

    """
    return self._config_get(self.component.page.theme.warning[1])

  @orange.setter
  def orange(self, value):
    self._config(value)

  @property
  def font_size(self):
    """
    Description:
    ------------

    Related Pages:

    """
    return self._config_get('none')

  @font_size.setter
  def font_size(self, value):
    self._config(value)

  @property
  def status(self):
    return self._config_get('none')

  @status.setter
  def status(self, value):
    if hasattr(self.component.page.theme, str(value)):
      color = getattr(self.component.page.theme, str(value))[1]
    else:
      color = self.component.page.theme.colors[-1]
    self._report.style.css.border_left = '5px solid %s' % color
    self._report.style.css.padding_left = 5
    self._config(value)

  @property
  def style_select(self):
    """
    Description:
    ------------
    Internal CSS class name to be used when the component is selected.
    """
    return self._config_get(None)

  @style_select.setter
  def style_select(self, value):
    self._config(value)


class OptionsTitle(OptionsText):

  @property
  def content_table(self):
    """
    Description:
    ------------

    Related Pages:

    """
    return self._config_get(True)

  @content_table.setter
  def content_table(self, flag):
    self._config(flag)


class OptionsNumber(OptionsText):

  @property
  def label(self):
    """
    Description:
    ------------
    The label attached to a number component.

    Attributes:
    ----------
    :prop text: String. The value.
    """
    return self._config_get("")

  @label.setter
  def label(self, text):
    self._config(text)

  @property
  def digits(self):
    """
    Description:
    ------------
    decimal point separator.

    Related Pages:

      http://openexchangerates.github.io/accounting.js/
    """
    return self._config_get(0)

  @digits.setter
  def digits(self, num):
    self._config(num)

  @property
  def format(self):
    """
    Description:
    ------------
    controls output: %s = symbol, %v = value/number.

    Related Pages:

      http://openexchangerates.github.io/accounting.js/
    """
    return self._config_get("%s%v")

  @format.setter
  def format(self, num):
    self._config(num)

  @property
  def symbol(self):
    """
    Description:
    ------------
    default currency symbol is ''.

    Related Pages:

      http://openexchangerates.github.io/accounting.js/#documentation
    """
    return self._config_get("")

  @symbol.setter
  def symbol(self, value):
    self._config("money", name="type_number")
    self._config(value)

  @property
  def thousand_sep(self):
    """
    Description:
    ------------
    thousands separator.

    Related Pages:

      http://openexchangerates.github.io/accounting.js/
    """
    return self._config_get(",")

  @thousand_sep.setter
  def thousand_sep(self, value):
    self._config(value)

  @property
  def decimal_sep(self):
    """
    Description:
    ------------
    decimal point separator.

    Related Pages:

      http://openexchangerates.github.io/accounting.js/
    """
    return self._config_get(".")

  @decimal_sep.setter
  def decimal_sep(self, value):
    self._config(value)


class OptionsNumberMoves(OptionsNumber):
  component_properties = ("css", "rotate", "font_size", "css_stats", "icon_up", "icon_down", "digits_percent")

  @property
  def css(self):
    """
    Description:
    ------------
    The label attached to a number component.

    Attributes:
    ----------
    :prop attrs: Dictionary. The CSS attributes.
    """
    return self._config_get({"text-align": "center", "margin-top": "5px",
                             "font-size": self.component.page.body.style.globals.font.normal(10)})

  @css.setter
  def css(self, attrs):
    self._config(attrs)

  @property
  def rotate(self):
    """
    Description:
    ------------

    Related Pages:

      https://www.w3schools.com/cssref/css3_pr_transform.asp
    """
    return self._config_get(40)

  @rotate.setter
  def rotate(self, value):
    self._config(value)

  @property
  def font_size(self):
    """
    Description:
    ------------
    The font size used by the percentage and difference.

    Related Pages:

      https://www.w3schools.com/cssref/css3_pr_transform.asp
    """
    return self._config_get(self.component.page.body.style.globals.font.normal(2))

  @font_size.setter
  def font_size(self, value):
    self._config(value)

  @property
  def css_stats(self):
    return self._config_get({})

  @css_stats.setter
  def css_stats(self, attrs):
    self._config(attrs)

  @property
  def icon_up(self):
    return self._config_get("fas fa-arrow-up")

  @icon_up.setter
  def icon_up(self, attrs):
    self._config(attrs)

  @property
  def icon_down(self):
    return self._config_get("")

  @icon_down.setter
  def icon_down(self, attrs):
    self._config(attrs)

  @property
  def digits_percent(self):
    return self._config_get(2)

  @digits_percent.setter
  def digits_percent(self, num):
    self._config(num)


class OptionsNumberDelta(OptionsNumber):
  component_properties = ("threshold1", "threshold2", "previous_label")

  @property
  def threshold1(self):
    """
    Description:
    ------------
    The first threshold.
    """
    return self._config_get(100)

  @threshold1.setter
  def threshold1(self, value):
    self._config(value)

  @property
  def threshold2(self):
    """
    Description:
    ------------
    The second threshold (smaller than the first one).
    """
    return self._config_get(50)

  @threshold2.setter
  def threshold2(self, value):
    self._config(value)

  @property
  def previous_label(self):
    """
    Description:
    ------------
    Set the label displayed before the previous value in the component.
    """
    return self._config_get("Previous number: ")

  @previous_label.setter
  def previous_label(self, value):
    self._config(value)


class OptionsLink(OptionsText):

  @property
  def url(self):
    """
    Description:
    ------------
    The href attribute specifies the URL of the page the link goes to.

    Related Pages:

      https://www.w3schools.com/tags/att_a_href.asp
    """
    return self._report.attr.get("href", '#')

  @url.setter
  def url(self, value):
    self._report.attr['href'] = value

  @property
  def href(self):
    """
    Description:
    ------------
    The href attribute specifies the URL of the page the link goes to.

    Related Pages:

      https://www.w3schools.com/tags/att_a_href.asp
    """
    return self._report.attr.get("href", '#')

  @href.setter
  def href(self, value):
    self._report.attr['href'] = value

  @property
  def target(self):
    """
    Description:
    ------------
    The target attribute specifies where to open the linked document.

    Related Pages:

      https://www.w3schools.com/tags/att_a_target.asp
    """
    return self._report.attr.get("target", '_self')

  @target.setter
  def target(self, value):
    self._report.attr['target'] = value


class OptionsConsole(OptionsText):

  @property
  def timestamp(self):
    """
    Description:
    ------------
    """
    return self.get(False)

  @timestamp.setter
  def timestamp(self, flag):
    self.set(flag)


class OptionsComposite(Options):

  @property
  def reset_class(self):
    """
    Description:
    ------------
    """
    return self.get(False)

  @reset_class.setter
  def reset_class(self, flag):
    self.set(flag)


class OptionsStatus(Options):

  @property
  def states(self):
    """
    Description:
    ------------
    """
    return self.get(False)

  @states.setter
  def states(self, flag):
    self.set(flag)

  @property
  def color(self):
    """
    Description:
    ------------
    """
    return self.get('white')

  @color.setter
  def color(self, color):
    self.set(color)

  @property
  def background(self):
    """
    Description:
    ------------
    """
    return self.get('grey')

  @background.setter
  def background(self, color):
    self.set(color)


class OptContents(Options):

  @property
  def manual(self):
    """
    Description:
    ------------
    Define the way the content table is updated.
    """
    return self.get("manual", False)

  @manual.setter
  def manual(self, flag):
    self.set(flag)


class OptBreadCrumb(Options):
  component_properties = ("delimiter", "style_selected")

  def set_style(self, name):
    """
    Description:
    ------------
    Set the breadcrumb to a predefined style.
    Do not hesitate to share on Github if you think that a new configuration should be promoted to the package.

    Attributes:
    ----------
    :param name: String. The predefined style.
    """
    defined_styles = {
      'pills': {
        "delimiter": '',
        "style": {"border-radius": "10px", "border": "1px solid %s" % self.component.page.theme.greys[4],
                  "background": self.component.page.theme.greys[0],
                  "margin": "0 2px", "width": '80px', "display": 'inline-block', "text-align": "center"},
        'selected': {"color": self.component.page.theme.greys[0], "background": self.component.page.theme.colors[-1]}},
      'tabs': {
        "delimiter": '',
        "style": {
          "border-bottom": "5px solid inherit",
          "margin": "0 2px", "width": '80px',
          "display": 'inline-block',
          "text-align": "center"},
        'selected': {
          "color": self.component.page.theme.success[1],
          "border-bottom": "5px solid %s" % self.component.page.theme.success[1]}},

    }
    self.style = defined_styles[name]["style"]
    self.delimiter = defined_styles[name]["delimiter"]
    self.style_selected = defined_styles[name]["selected"]

  @property
  def delimiter(self):
    """
    Description:
    ------------
    Set the delimiter for the breadcrumb categories.

    Attributes:
    ----------
    :prop value: String. The delimiter. Default /.
    """
    return self._config_get(' / ')

  @delimiter.setter
  def delimiter(self, value):
    self._config(value)

  @property
  def height(self):
    """
    Description:
    ------------
    Set the height for the breadcrumb items.

    Attributes:
    ----------
    :prop number: Integer. The height in pixel. Default 0.
    """
    return self._config_get(0)

  @height.setter
  def height(self, number):
    self._config(number)

  @property
  def style_selected(self):
    """
    Description:
    ------------
    Set the style for the selected item.
    This style will be added on top of the common CSS style.

    Related Pages:

      https://www.w3schools.com/cssref/

    Attributes:
    ----------
    :prop values: Dictionary. The CSS styles.
    """
    return self._config_get({})

  @style_selected.setter
  def style_selected(self, values):
    self._config(values)


class OptionsHighlights(Options):
  component_properties = ("close", "markdown")

  @property
  def close(self):
    """
    Description:
    ------------

    Related Pages:
    """
    return self._config_get(True)

  @close.setter
  def close(self, flag):
    self._config(flag)

  @property
  def reset(self):
    """
    Description:
    ------------

    Related Pages:
    """
    return self._config_get(False)

  @reset.setter
  def reset(self, flag):
    self._config(flag)

  @property
  def markdown(self):
    """
    Description:
    ------------
    Showdown is a Javascript Markdown to HTML converter, based on the original works by John Gruber.
    Showdown can be used client side (in the browser) or server side (with NodeJs).

    Related Pages:

      https://github.com/showdownjs/showdown
    """
    return self._config_get(False)

  @markdown.setter
  @packageImport("showdown")
  def markdown(self, values):
    if isinstance(values, bool):
      self._config(values)
      self._config({} if values is True else values, 'showdown')
    else:
      self._config(True)
      self._config(values, 'showdown')

  @property
  def showdown(self):
    """
    Description:
    ------------
    Showdown is a Javascript Markdown to HTML converter, based on the original works by John Gruber.
    Showdown can be used client side (in the browser) or server side (with NodeJs).

    Related Pages:

      https://github.com/showdownjs/showdown
    """
    return self._config_get(False)

  @showdown.setter
  @packageImport("showdown")
  def showdown(self, values):
    self._config(True, 'markdown')
    self._config(values)


class OptSearchResult(Options):
  component_properties = ("title", "dsc", "url", "visited", "link")

  @property
  def title(self):
    """
    Description:
    ------------

    Related Pages:
    """
    return self._config_get({
      'color': self.component.page.theme.colors[-1], "font-weight": 900,
      'font-size': '18px'})

  @title.setter
  def title(self, attrs):
    self._config(attrs)

  @property
  def dsc(self):
    """
    Description:
    ------------

    Related Pages:
    """
    return self._config_get(
      {'color': self.component.page.theme.greys[6], "padding-bottom": "10px"})

  @dsc.setter
  def dsc(self, attrs):
    self._config(attrs)

  @property
  def url(self):
    """
    Description:
    ------------

    Related Pages:
    """
    return self._config_get(
      {"font-style": 'italic', 'color': self.component.page.theme.notch(), 'font-size': '14px'})

  @url.setter
  def url(self, attrs):
    self._config(attrs)

  @property
  def visited(self):
    """
    Description:
    ------------

    Related Pages:
    """
    return self._config_get({'color': self.component.page.theme.greys[5]})

  @visited.setter
  def visited(self, attrs):
    self._config(attrs)

  @property
  def link(self):
    """
    Description:
    ------------

    Related Pages:
    """
    return self._config_get({'color': self.component.page.theme.colors[7], 'cursor': 'pointer'})

  @link.setter
  def link(self, attrs):
    self._config(attrs)

  @property
  def pageNumber(self):
    """
    Description:
    ------------

    Related Pages:
    """
    return self._config_get(0)

  @pageNumber.setter
  def pageNumber(self, num):
    self._config(num)

  @property
  def currPage(self):
    """
    Description:
    ------------

    Related Pages:
    """
    return self._config_get(0)

  @currPage.setter
  def currPage(self, num):
    self._config(num)

  @property
  def grey(self):
    """
    Description:
    ------------

    Related Pages:
    """
    return self._config_get(self.component.page.theme.colors[9])

  @grey.setter
  def grey(self, color):
    self._config(color)

  @property
  def white(self):
    """
    Description:
    ------------

    Related Pages:
    """
    return self._config_get(self.component.page.theme.colors[0])

  @white.setter
  def white(self, color):
    self._config(color)
