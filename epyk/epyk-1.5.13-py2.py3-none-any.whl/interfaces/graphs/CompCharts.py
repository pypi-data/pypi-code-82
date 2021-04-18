#!/usr/bin/python
# -*- coding: utf-8 -*-


from epyk.core import html

from epyk.interfaces.graphs import CompChartsApex
from epyk.interfaces.graphs import CompChartsBillboard
from epyk.interfaces.graphs import CompChartsDc
from epyk.interfaces.graphs import CompChartsC3
from epyk.interfaces.graphs import CompChartsChartJs
from epyk.interfaces.graphs import CompChartsPlotly
from epyk.interfaces.graphs import CompChartsNvd3
from epyk.interfaces.graphs import CompChartsD3
from epyk.interfaces.graphs import CompChartsVis
from epyk.interfaces.graphs import CompChartsSvg
from epyk.interfaces.graphs import CompChartsCanvas
from epyk.interfaces.graphs import CompChartsGoogle
from epyk.interfaces.graphs import CompChartsSparkline


class Graphs:

  def __init__(self, ui):
    self.page = ui.page

  def plot(self, pkg="apex", record=None, y=None, x=None, kind="line", profile=None, width=(100, "%"),
           height=(330, "px"), options=None, html_code=None):
    """
    Description:
    ------------

    Usage:
    -----

    Attributes:
    ----------
    :param pkg: String. Optional. The external chart package reference. Default ApexCharts.
    :param record: List. Optional. The list of dictionaries with the input data.
    :param y: List | String. Optional. The columns corresponding to keys in the dictionaries in the record.
    :param x: String. Optional. The column corresponding to a key in the dictionaries in the record.
    :param kind: String. Optional. The chart type.
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage.
    :param width: Tuple. Optional. The width of the component in the page, default (100, '%').
    :param height: Tuple. Optional. The height of the component in the page, default (330, "px").
    :param options: Dictionary. Optional. Specific Python options available for this component.
    :param html_code: String. Optional. An identifier for this component (on both Python and Javascript side).
    """
    if y is not None and not isinstance(y, list):
      y = [y]
    chart_pkg = getattr(self, pkg)
    return getattr(chart_pkg, kind)(record=record, y_columns=y, x_axis=x, profile=profile, width=width, height=height,
                                    options=options, html_code=html_code)

  @html.Html.css_skin()
  def skillbars(self, records=None, y_column=None, x_axis=None, title=None, width=(100, '%'),
                height=(None, 'px'), html_code=None, options=None, profile=False):
    """
    Description:
    ------------
    Python interface for the HTML Skill bars, simple bars chart done in pure Javascript and CSS.

    Usage:
    -----

      records = [
        {"label": 'python', 'value': 12},
        {"label": 'Java', 'value': 5},
        {"label": 'Javascript', 'value': 80}]
      page.ui.charts.skillbars(records, y_column='value', x_axis='label').css({"width": '100px'})

    Related Pages:

      https://www.w3schools.com/howto/howto_css_skill_bar.asp

    Attributes:
    ----------
    :param records:
    :param y_column:
    :param x_axis:
    :param title:
    :param width: Tuple. Optional. A tuple with the integer for the component width and its unit.
    :param height: Tuple. Optional. A tuple with the integer for the component height and its unit.
    :param html_code: String. Optional. An identifier for this component (on both Python and Javascript side).
    :param options: Dictionary. Optional. Specific Python options available for this component.
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage.
    """
    if y_column is None or x_axis is None:
      raise Exception("seriesName and axis must be defined")

    options = options or {}
    html_skillbar = html.HtmlEvent.SkillBar(
      self.page, records, y_column, x_axis, title, width, height, html_code, options, profile)
    return html_skillbar

  @html.Html.css_skin()
  def sparkline(self, chart_type, data, title=None, options=None, width=(None, "%"), height=(None, "px"),
                profile=False):
    """
    Description:
    ------------
    Display a sparkline component.

    Usage:
    -----

      page.ui.charts.sparkline("box", [1, 2, 3, 4, 5, 4, 3, 2, 1])
      page.ui.charts.sparkline("bar", [1, 2, 3, 4, 5, 4, 3, 2, 10])

    Related Pages:

      https://omnipotent.net/jquery.sparkline/#s-about

    Attributes:
    ----------
    :param chart_type: The type of chart (bullet, line, bar, tristate, discrete, pie, box)
    :param data: String. A String corresponding to a JavaScript object.
    :param options: Dictionary. Optional. Specific Python options available for this component.
    :param width: Tuple. Optional. A tuple with the integer for the component width and its unit.
    :param height: Tuple. Optional. A tuple with the integer for the component height and its unit.
    :param title: String. Optional. A panel title. This will be attached to the title property.
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage.

    :return: A python Sparkline object
    """
    dfl_options = {"type": chart_type}
    if options is not None:
      dfl_options.update(options)
    html_chart = html.graph.GraphSparklines.Sparklines(
      self.page, data, title, width, height, dfl_options, profile)
    html_chart.color(self.page.theme.charts[0])
    return html_chart

  @property
  def sparklines(self):
    """
    Description:
    ------------
    Built on top of d3.js and stack.gl, Plotly.js is a high-level, declarative charting library.
    plotly.js ships with over 40 chart types, including 3D charts, statistical graphs, and SVG maps.

    Usage:
    -----

    Related Pages:

      https://plotly.com/javascript/

    :return: A Python Plolty object
    """
    return CompChartsSparkline.Sparkline(self)

  @property
  def plotly(self):
    """
    Description:
    ------------
    Built on top of d3.js and stack.gl, Plotly.js is a high-level, declarative charting library.
    plotly.js ships with over 40 chart types, including 3D charts, statistical graphs, and SVG maps.

    Usage:
    -----

    Related Pages:

      https://plotly.com/javascript/

    :return: A Python Plolty object
    """
    return CompChartsPlotly.Plotly(self)

  @property
  def chartJs(self):
    """
    Description:
    ------------
    Simple yet flexible JavaScript charting for designers & developers.

    Usage:
    -----

    Related Pages:

      https://www.chartjs.org/

    :return: A Python ChartJs object
    """
    return CompChartsChartJs.ChartJs(self)

  @property
  def apex(self):
    """
    Description:
    ------------
    Interface for the ApexChart library.

    Usage:
    -----

    Related Pages:

      https://apexcharts.com/

    :return: A Python ChartJs object
    """
    return CompChartsApex.ApexChart(self)

  @property
  def c3(self):
    """
    Description:
    ------------
    Interface to the JavaScript C3 module.

    Usage:
    -----

      page.ui.charts.billboard.line(x_axis="Date")

    Related Pages:

      https://c3js.org/

    :return: A Python C3 object
    """
    return CompChartsC3.C3(self)

  @property
  def bb(self):
    """
    Description:
    ------------
    Interface to the Javascript Billboard module.

    This will propose various charts for data analysis and visualisation based on D£.
    This project has been forked from C3.js.

    Usage:
    -----

    Related Pages:

      https://naver.github.io/billboard.js/

    :return: A Python Billboard Object
    """
    return CompChartsBillboard.Billboard(self)

  @property
  def billboard(self):
    """
    Description:
    ------------
    Interface to the Javascript Billboard module.

    This will propose various charts for data analysis and visualisation based on D£.
    This project has been forked from C3.js.

    Usage:
    -----

    Related Pages:

      https://naver.github.io/billboard.js/

    :return: A Python Billboard Object
    """
    return CompChartsBillboard.Billboard(self)

  @property
  def vis(self):
    """
    Description:
    ------------
    A dynamic, browser based visualization library.

    Usage:
    -----

    Related Pages:

      https://visjs.org/

    :return: A Python Vis object
    """
    return CompChartsVis.Vis(self)

  @property
  def nvd3(self):
    """
    Description:
    ------------
    Interface to the Javascript NVD3 library.

    Usage:
    -----

    Related Pages:

      http://nvd3.org/

    :return: A Python NVD3 object
    """
    return CompChartsNvd3.Nvd3(self)

  @property
  def dc(self):
    """
    Description:
    ------------
    dc.js is a javascript charting library with native crossfilter support,
    allowing highly efficient exploration on large multi-dimensional datasets (inspired by crossfilter's demo).

    Usage:
    -----

    Related Pages:

      https://dc-js.github.io/dc.js/
    """
    return CompChartsDc.DC(self)

  @property
  def d3(self):
    """
    Description:
    ------------
    D3.js is a JavaScript library for manipulating documents based on data.

    Usage:
    -----

    Related Pages:

      https://d3js.org/
    """
    return CompChartsD3.D3(self)

  @property
  def google(self):
    """
    Description:
    ------------
    Google chart tools are powerful, simple to use, and free.
    Try out our rich gallery of interactive charts and data tools.

    Usage:
    -----

    Related Pages:

      https://developers.google.com/chart
    """
    if not getattr(self.page, '_with_google_imports', False):
      raise Exception("Google produce must be added using for example page.imports.google_products(['charts'])")

    return CompChartsGoogle.ChartGoogle(self)

  @property
  def svg(self):
    """
    Description:
    ------------
    SVG defines vector-based graphics in XML format.

    Usage:
    -----

    Related Pages:

      https://www.w3schools.com/graphics/svg_intro.asp
    """
    return CompChartsSvg.SVG(self)

  @property
  def canvas(self):
    """
    Description:
    ------------
    The HTML <canvas> element is used to draw graphics on a web page.

    The graphic to the left is created with <canvas>.
    It shows four elements: a red rectangle, a gradient rectangle, a multicolor rectangle, and a multicolor text.

    Usage:
    -----

    Related Pages:

      https://www.w3schools.com/html/html5_canvas.asp
    """
    return CompChartsCanvas.Canvas(self)

  @html.Html.css_skin()
  def menu(self, chart, height=(18, 'px'), options=None, post=None, profile=None):
    """
    Description:
    -----------
    Add a standard menu on the table to trigger standard operation (add, empty, copy, download).

    Usage:
    -----

    Attributes:
    ----------
    :param chart:
    :param height:
    :param options: Dictionary. Optional. Specific Python options available for this component.
    :param post:
    :param profile:
    """
    # ("Csv", "fas fa-file-csv")
    commands = [("Clear", "fas fa-trash-alt")]
    menu_items = []
    options = options or {}
    for typ, icon in commands:
      if icon:
        if isinstance(icon, tuple):
          icon = icon[0]
        r = self.page.ui.icons.awesome(
          icon, text=typ, height=height, width=(35, 'px'), options=options, profile=profile)
        r.span.style.css.line_height = r.style.css.height
        r.icon.style.css.font_factor(-5)
        r.style.css.font_factor(-5)
        r.span.style.css.margin = "0 2px -3px -3px"
        if typ == "Csv":
          r.click([chart.js.download("csv", "data.csv")])
        elif typ == "Clear":
          r.click([chart.js.clearData()])
        menu_items.append(r)
    container = self.page.ui.menu(chart, menu_items=menu_items, copy=False, post=post, editable=False)
    return container


class Chart2d:

  def __init__(self, ui):
    self.page = ui.page

  @property
  def plotly(self):
    """
    Description:
    ------------
    Built on top of d3.js and stack.gl, Plotly.js is a high-level, declarative charting library.
    plotly.js ships with over 40 chart types, including 3D charts, statistical graphs, and SVG maps.

    Usage:
    -----

    Related Pages:

      https://plotly.com/javascript/

    :return: A Python Plolty object
    """
    return CompChartsPlotly.Plotly2D(self)

  @property
  def nvd3(self):
    """
    Description:
    ------------
    This project is an attempt to build re-usable charts and chart components for d3.js
    without taking away the power that d3.js gives you.

    Usage:
    -----

    Related Pages:

      http://nvd3.org/

    :return: A Python NVD3 object
    """
    return CompChartsNvd3.Nvd3(self)

  @property
  def dc(self):
    """
    Description:
    ------------
    dc.js is a javascript charting library with native crossfilter support, allowing highly
    efficient exploration on large multi-dimensional datasets (inspired by crossfilter's demo).

    Usage:
    -----

    Related Pages:

      https://dc-js.github.io/dc.js/
    """
    return CompChartsDc.DC(self)

  @property
  def d3(self):
    """
    Description:
    ------------
    D3.js is a JavaScript library for manipulating documents based on data.

    Usage:
    -----

    Related Pages:

      https://d3js.org/
    """
    return CompChartsD3.D3(self)

  @property
  def svg(self):
    """
    Description:
    ------------
    SVG stands for Scalable Vector Graphics.

    SVG defines vector-based graphics in XML format.

    Usage:
    -----

    Related Pages:

      https://www.w3schools.com/graphics/svg_intro.asp
    """
    return CompChartsSvg.SVG(self)

  @property
  def canvas(self):
    """
    Description:
    ------------
    The HTML <canvas> element is used to draw graphics on a web page.

    The graphic to the left is created with <canvas>.
    It shows four elements: a red rectangle, a gradient rectangle, a multicolor rectangle, and a multicolor text.

    Usage:
    -----

    Related Pages:

      https://www.w3schools.com/html/html5_canvas.asp
    """
    return CompChartsCanvas.Canvas(self)

  @property
  def chartJs(self):
    """
    Description:
    ------------
    Interface for the ChartJs library

    Usage:
    -----

    Related Pages:

      https://www.chartjs.org/

    :return: A Python ChartJs object
    """
    return CompChartsChartJs.ChartJs(self)

  @property
  def apex(self):
    """
    Description:
    ------------
    Interface for the ApexChart library.

    Usage:
    -----

    Related Pages:

      https://apexcharts.com/

    :return: A Python ChartJs object
    """
    return CompChartsApex.ApexChart(self)

  @property
  def c3(self):
    """
    Description:
    ------------
    Interface to the JavaScript C3 module

    Usage:
    -----

    Related Pages:

      https://c3js.org/

    :return: A Python C3 object
    """
    return CompChartsC3.C3(self)

  @property
  def billboard(self):
    """
    Description:
    ------------
    Interface to the Javascript Billboard module.

    This will propose various charts for data analysis and visualisation based on D£.
    This project has been forked from Billboard.js.

    Usage:
    -----

    Related Pages:

      https://naver.github.io/billboard.js/

    :return: A Python Billboard Object
    """
    return CompChartsBillboard.Billboard(self)

  @property
  def vis(self):
    """
    Description:
    ------------
    Interface for the Vis library.

    Usage:
    -----

    Related Pages:

      https://visjs.org/

    :return: A Python Vis object
    """
    return CompChartsVis.Vis2D(self)


class Chart3d:

  def __init__(self, ui):
    self.page = ui.page

  @property
  def plotly(self):
    """
    Description:
    ------------
    Built on top of d3.js and stack.gl, Plotly.js is a high-level, declarative charting library.
    plotly.js ships with over 40 chart types, including 3D charts, statistical graphs, and SVG maps.

    Usage:
    -----

    Related Pages:

      https://plotly.com/javascript/

    :return: A Python Plolty object
    """
    return CompChartsPlotly.Plotly3D(self)

  @property
  def vis(self):
    """
    Description:
    ------------
    Interface for the Vis library.

    Usage:
    -----

    Related Pages:

      https://visjs.org/

    :return: A Python Vis object
    """
    return CompChartsVis.Vis3D(self)
