
from epyk.core.css.styles import GrpCls
from epyk.core.css import Classes


class DataTableThemes:

  def __init__(self, classlist):
    self.classlist = classlist

  def cell_border(self):
    """
    Description:
    -----------

    Related Pages:

      https://datatables.net/examples/styling/cell-border.html
    """
    self.classlist.add("cell-border")
    return self

  def compact(self):
    """
    Description:
    -----------
    Reduce the amount of white-space the default styling for the DataTable uses, increasing the information density on
    screen, as shown below.
    Note that this style requires DataTables 1.10.1 or newer.

    Related Pages:

      https://datatables.net/manual/styling/classes
    """
    self.classlist.add("compact")
    return self

  def display_compact(self):
    """
    Description:
    -----------

    Related Pages:

      https://datatables.net/examples/styling/compact.html
    """
    self.classlist.add("display")
    self.classlist.add("compact")
    return self

  def hover(self):
    """
    Description:
    -----------

    Related Pages:

      https://datatables.net/examples/styling/hover.html
    """
    self.classlist.add("hover")
    return self

  def order_column(self):
    """
    Description:
    -----------
    Highlight the ordering column.

    Related Pages:

      https://datatables.net/examples/styling/order-column.html
    """
    self.classlist.add("order-column")
    return self

  def nowrap(self):
    """
    Description:
    -----------
    Disable line wrapping of content in the table cells, so the text will always appear on one line.
    Note that this style requires DataTables 1.10.1 or newer.

    Related Pages:

      https://datatables.net/manual/styling/classes
    """
    self.classlist.add("nowrap")
    return self

  def row_border(self):
    """
    Description:
    -----------
    Border on the rows only.

    Related Pages:

      https://datatables.net/examples/styling/row-border.html
    """
    self.classlist.add("row-border")
    return self

  def stripe(self):
    """
    Description:
    -----------
    Row striping.

    Related Pages:

      https://datatables.net/examples/styling/stripe.html
    """
    self.classlist.add("stripe")
    return self

  def bootstrap(self):
    """
    Description:
    -----------

    Related Pages:

      https://datatables.net/examples/styling/bootstrap4.html
    """
    self.classlist.add("table")
    self.classlist.add("table-striped")
    self.classlist.add("table-bordered")
    return self


class Datatable(GrpCls.ClassHtml):

  def __init__(self, component):
    super(Datatable, self).__init__(component)
    self._css_datatable, self._css_datatable_header, self._css_datatable_row_odd = None, None, None
    self._css_datatable_row_even, self._css_datatable_footer = None, None
    self.classList['main'].add(self.cls_datatable)
    self.classList['main'].add(self.cls_datatable_header)
    self.classList['main'].add(self.cls_datatable_odd)
    self.classList['main'].add(self.cls_datatable_even)
    self.classList['main'].add(self.cls_datatable_footer)

  @property
  def themes(self):
    """
    Description:
    -----------
    Add the predefined themes in the javascript library.

    Related Pages:

      https://datatables.net/examples/styling/index.html
    """
    return DataTableThemes(self.classList['main'])

  @property
  def cls_datatable(self):
    """
    Description:
    -----------

    :rtype: Classes.CatalogTable.CatalogTable
    """
    if self._css_datatable is None:
      self._css_datatable = Classes.CatalogTable.CatalogTable(self.component.page, self.classList['main']).datatable()
    return self._css_datatable

  @property
  def cls_datatable_header(self):
    """
    Description:
    -----------

    :rtype: Classes.CatalogTable.CatalogTable
    """
    if self._css_datatable_header is None:
      self._css_datatable_header = Classes.CatalogTable.CatalogTable(
        self.component.page, self.classList['main']).datatable_header()
    return self._css_datatable_header

  @property
  def cls_datatable_odd(self):
    """
    Description:
    -----------

    :rtype: Classes.CatalogTable.CatalogTable
    """
    if self._css_datatable_row_odd is None:
      self._css_datatable_row_odd = Classes.CatalogTable.CatalogTable(
        self.component.page, self.classList['main']).datatable_odd()
    return self._css_datatable_row_odd

  @property
  def cls_datatable_even(self):
    """
    Description:
    -----------

    :rtype: Classes.CatalogTable.CatalogTable
    """
    if self._css_datatable_row_even is None:
      self._css_datatable_row_even = Classes.CatalogTable.CatalogTable(
        self.component.page, self.classList['main']).datatable_even()
    return self._css_datatable_row_even

  @property
  def cls_datatable_footer(self):
    """
    Description:
    -----------

    :rtype: Classes.CatalogTable.CatalogTable
    """
    if self._css_datatable_footer is None:
      self._css_datatable_footer = Classes.CatalogTable.CatalogTable(
        self.component.page, self.classList['main']).datatable_footer()
    return self._css_datatable_footer


class Tabulator(GrpCls.ClassHtml):

  def __init__(self, component):
    super(Tabulator, self).__init__(component)
    self._css_tabulator, self._css_tabulator_row, self._css_tabulator_header = None, None, None
    self._css_tabulator_even_row, self._css_tabulator_cell, self._css_tabulator_headers = None, None, None
    self._css_tabulator_col, self._css_tabulator_col_content, self._css_tabulator_selected = None, None, None
    self._css_tb_odd_row, self._css_tb_groups, self._css_tb_footer, self._css_tabulator_menu_item = 4 * [None]
    self._css_tb_footer_pg, self._css_tb_tree, self._css_tb_tree_exp, self._css_tabulator_menu = 4 * [None]
    self._css_tabulator_even_row_no_strip, self._css_tabulator_editing, self._css_tabulator_cell_editing = 3 * [None]
    self._css_sorter_asc, self._css_sorter_desc, self._css_sorter_none = 3 * [None]
    self.__strip = False
    self.classList['main'].add(self.cls_tabulator)
    self.classList['other'].add(self.cls_tabulator_row)
    self.classList['other'].add(self.cls_tabulator_header)
    self.classList['other'].add(self.cls_tabulator_cell)
    self.classList['other'].add(self.cls_tabulator_headers)
    self.classList['other'].add(self.cls_tabulator_col)
    self.classList['other'].add(self.cls_tabulator_col_content)
    self.classList['other'].add(self.cls_tabulator_selected)
    self.classList['other'].add(self.cls_tb_even_row)
    self.classList['other'].add(self.cls_tb_groups)
    self.classList['other'].add(self.cls_tb_footer)
    self.classList['other'].add(self.cls_tb_footer_pg)
    self.classList['other'].add(self.cls_tb_tree)
    self.classList['other'].add(self.cls_tb_tree_exp)
    self.classList['other'].add(self.cls_tabulator_menu)
    self.classList['other'].add(self.cls_tabulator_menu_item)
    self.classList['other'].add(self.cls_tabulator_editing)
    self.classList['other'].add(self.cls_tabulator_cell_editing)
    self.classList['other'].add(self.cls_sorter_asc)
    self.classList['other'].add(self.cls_sorter_desc)
    self.classList['other'].add(self.cls_sorter_none)

  def strip(self):
    """
    Description:
    -----------

    """
    self.__strip = True
    self.classList['main'].add(self.cls_tabulator_even_row)

  @property
  def cls_tabulator(self):
    """
    Description:
    -----------

    :rtype: Classes.CatalogTable.CatalogTable
    """
    if self._css_tabulator is None:
      self._css_tabulator = Classes.CatalogTable.CatalogTable(
        self.component.page, self.classList['main']).tabulator()
    return self._css_tabulator

  @property
  def cls_sorter_asc(self):
    """
    Description:
    -----------

    :rtype: Classes.CatalogTable.CatalogTable
    """
    if self._css_sorter_asc is None:
      self._css_sorter_asc = Classes.CatalogTable.CatalogTable(
        self.component.page, self.classList['main']).tabulator_sorter_asc()
    return self._css_sorter_asc

  @property
  def cls_sorter_desc(self):
    """
    Description:
    -----------

    :rtype: Classes.CatalogTable.CatalogTable
    """
    if self._css_sorter_desc is None:
      self._css_sorter_desc = Classes.CatalogTable.CatalogTable(
        self.component.page, self.classList['main']).tabulator_sorter_desc()
    return self._css_sorter_desc

  @property
  def cls_sorter_none(self):
    """
    Description:
    -----------

    :rtype: Classes.CatalogTable.CatalogTable
    """
    if self._css_sorter_none is None:
      self._css_sorter_none = Classes.CatalogTable.CatalogTable(
        self.component.page, self.classList['main']).tabulator_sorter_none()
    return self._css_sorter_none

  @property
  def cls_tabulator_row(self):
    """
    Description:
    -----------

    :rtype: Classes.CatalogTable.CatalogTable
    """
    if self._css_tabulator_row is None:
      self._css_tabulator_row = Classes.CatalogTable.CatalogTable(
        self.component.page, self.classList['other']).tabulator_rows()
    return self._css_tabulator_row

  @property
  def cls_tabulator_cell(self):
    """
    Description:
    -----------

    :rtype: Classes.CatalogTable.CatalogTable
    """
    if self._css_tabulator_cell is None:
      self._css_tabulator_cell = Classes.CatalogTable.CatalogTable(
        self.component.page, self.classList['other']).tabulator_cell()
    return self._css_tabulator_cell

  @property
  def cls_tabulator_col(self):
    """
    Description:
    -----------

    :rtype: Classes.CatalogTable.CatalogTable
    """
    if self._css_tabulator_col is None:
      self._css_tabulator_col = Classes.CatalogTable.CatalogTable(
        self.component.page, self.classList['other']).tabulator_col()
    return self._css_tabulator_col

  @property
  def cls_tabulator_col_content(self):
    """
    Description:
    -----------

    :rtype: Classes.CatalogTable.CatalogTable
    """
    if self._css_tabulator_col_content is None:
      self._css_tabulator_col_content = Classes.CatalogTable.CatalogTable(
        self.component.page, self.classList['other']).tabulator_col_content()
    return self._css_tabulator_col_content

  @property
  def cls_tabulator_menu(self):
    """
    Description:
    -----------

    :rtype: Classes.CatalogTable.CatalogTable
    """
    if self._css_tabulator_menu is None:
      self._css_tabulator_menu = Classes.CatalogTable.CatalogTable(
        self.component.page, self.classList['other']).tabulator_menu()
    return self._css_tabulator_menu

  @property
  def cls_tabulator_menu_item(self):
    """
    Description:
    -----------

    :rtype: Classes.CatalogTable.CatalogTable
    """
    if self._css_tabulator_menu_item is None:
      self._css_tabulator_menu_item = Classes.CatalogTable.CatalogTable(
        self.component.page, self.classList['other']).tabulator_menu_item()
    return self._css_tabulator_menu_item

  @property
  def cls_tabulator_selected(self):
    """
    Description:
    -----------

    :rtype: Classes.CatalogTable.CatalogTable
    """
    if self._css_tabulator_selected is None:
      self._css_tabulator_selected = Classes.CatalogTable.CatalogTable(
        self.component.page, self.classList['other']).tabulator_selected()
    return self._css_tabulator_selected

  @property
  def cls_tabulator_even_row(self):
    """
    Description:
    -----------

    :rtype: Classes.CatalogTable.CatalogTable
    """
    if self._css_tabulator_even_row is None:
      self._css_tabulator_even_row = Classes.CatalogTable.CatalogTable(
        self.component.page, self.classList['main']).tabulator_even_rows()
    return self._css_tabulator_even_row

  @property
  def cls_tabulator_even_row_no_strip(self):
    """
    Description:
    -----------

    :rtype: Classes.CatalogTable.CatalogTable
    """
    if self._css_tabulator_even_row_no_strip is None:
      self._css_tabulator_even_row_no_strip = Classes.CatalogTable.CatalogTable(
        self.component.page, self.classList['main']).tabulator_even_rows_no_strop()
    return self._css_tabulator_even_row_no_strip

  @property
  def cls_tb_even_row(self):
    """
    Description:
    -----------

    :rtype: Classes.CatalogTable.CatalogTable
    """
    if self._css_tb_odd_row is None:
      self._css_tb_odd_row = Classes.CatalogTable.CatalogTable(
        self.component.page, self.classList['other']).tabulator_odd_rows()
    return self._css_tb_odd_row

  @property
  def cls_tb_groups(self):
    """
    Description:
    -----------

    :rtype: Classes.CatalogTable.CatalogTable
    """
    if self._css_tb_groups is None:
      self._css_tb_groups = Classes.CatalogTable.CatalogTable(
        self.component.page, self.classList['other']).tabulator_groups()
    return self._css_tb_groups

  @property
  def cls_tb_footer(self):
    """
    Description:
    -----------

    :rtype: Classes.CatalogTable.CatalogTable
    """
    if self._css_tb_footer is None:
      self._css_tb_footer = Classes.CatalogTable.CatalogTable(
        self.component.page, self.classList['other']).tabulator_footer()
    return self._css_tb_footer

  @property
  def cls_tb_footer_pg(self):
    """
    Description:
    -----------

    :rtype: Classes.CatalogTable.CatalogTable
    """
    if self._css_tb_footer_pg is None:
      self._css_tb_footer_pg = Classes.CatalogTable.CatalogTable(
        self.component.page, self.classList['other']).tabulator_footer_pagination()
    return self._css_tb_footer_pg

  @property
  def cls_tb_tree(self):
    """
    Description:
    -----------

    :rtype: Classes.CatalogTable.CatalogTable
    """
    if self._css_tb_tree is None:
      self._css_tb_tree = Classes.CatalogTable.CatalogTable(
        self.component.page, self.classList['other']).tabulator_tree_control()
    return self._css_tb_tree

  @property
  def cls_tb_tree_exp(self):
    """
    Description:
    -----------

    :rtype: Classes.CatalogTable.CatalogTable
    """
    if self._css_tb_tree_exp is None:
      self._css_tb_tree_exp = Classes.CatalogTable.CatalogTable(
        self.component.page, self.classList['other']).tabulator_tree_control_expand()
    return self._css_tb_tree_exp

  @property
  def cls_tabulator_header(self):
    """
    Description:
    -----------

    :rtype: Classes.CatalogTable.CatalogTable
    """
    if self._css_tabulator_header is None:
      self._css_tabulator_header = Classes.CatalogTable.CatalogTable(
        self.component.page, self.classList['other']).tabulator_header()
    return self._css_tabulator_header

  @property
  def cls_tabulator_editing(self):
    """
    Description:
    -----------

    :rtype: Classes.CatalogTable.CatalogTable
    """
    if self._css_tabulator_editing is None:
      self._css_tabulator_editing = Classes.CatalogTable.CatalogTable(
        self.component.page, self.classList['other']).tabulator_editing()
    return self._css_tabulator_editing

  @property
  def cls_tabulator_cell_editing(self):
    """
    Description:
    -----------

    :rtype: Classes.CatalogTable.CatalogTable
    """
    if self._css_tabulator_cell_editing is None:
      self._css_tabulator_cell_editing = Classes.CatalogTable.CatalogTable(
        self.component.page, self.classList['other']).tabulator_cell_editing()
    return self._css_tabulator_cell_editing

  @property
  def cls_tabulator_headers(self):
    """
    Description:
    -----------

    :rtype: Classes.CatalogTable.CatalogTable
    """
    if self._css_tabulator_headers is None:
      self._css_tabulator_headers = Classes.CatalogTable.CatalogTable(
        self.component.page, self.classList['other']).tabulator_headers()
    return self._css_tabulator_headers

  def get_classes_css(self):
    """
    Description:
    -----------

    :return:
    """
    if not self.__strip:
      self.classList['main'].add(self.cls_tabulator_even_row_no_strip)
    return super(Tabulator, self).get_classes_css()


class Pivot(GrpCls.ClassHtml):

  def __init__(self, component):
    super(Pivot, self).__init__(component)
    self._css_pt_head, self._css_pt_cell, self._css_pt_axis = 3 * [None]
    self._css_pt_box, self._css_pt_pop, self._css_pt_val, self._css_pt_label = 4 * [None]
    self._css_pt_pop_header, self._css_pt_pop_button, self._css_pt_pop_checks = 3 * [None]
    self._css_pt_pop_checks_label = None
    self.classList['main'].add(self.cls_pt_head)
    self.classList['other'].add(self.cls_pt_cell)
    self.classList['other'].add(self.cls_pt_axis)
    self.classList['other'].add(self.cls_pt_filter_box)
    self.classList['other'].add(self.cls_pt_popup)
    self.classList['other'].add(self.cls_pt_val)
    self.classList['other'].add(self.cls_pt_label)
    self.classList['other'].add(self.cls_pt_popup_header)
    self.classList['other'].add(self.cls_pt_popup_button)
    self.classList['other'].add(self.cls_pt_popup_checks)
    self.classList['other'].add(self.cls_pt_popup_checks_label)

  @property
  def cls_pt_popup_checks_label(self):
    """
    Description:
    -----------

    :rtype: Classes.CatalogTable.CatalogTable
    """
    if self._css_pt_pop_checks_label is None:
      self._css_pt_pop_checks_label = Classes.CatalogTable.CatalogTable(
        self.component.page, self.classList['other']).pivot_filter_popup_checks_label()
    return self._css_pt_pop_checks_label

  @property
  def cls_pt_popup_checks(self):
    """
    Description:
    -----------

    :rtype: Classes.CatalogTable.CatalogTable
    """
    if self._css_pt_pop_checks is None:
      self._css_pt_pop_checks = Classes.CatalogTable.CatalogTable(
        self.component.page, self.classList['other']).pivot_filter_popup_checks()
    return self._css_pt_pop_checks

  @property
  def cls_pt_head(self):
    """
    Description:
    -----------

    :rtype: Classes.CatalogTable.CatalogTable
    """
    if self._css_pt_head is None:
      self._css_pt_head = Classes.CatalogTable.CatalogTable(
        self.component.page, self.classList['main']).pivot_head()
    return self._css_pt_head

  @property
  def cls_pt_cell(self):
    """
    Description:
    -----------

    :rtype: Classes.CatalogTable.CatalogTable
    """
    if self._css_pt_cell is None:
      self._css_pt_cell = Classes.CatalogTable.CatalogTable(
        self.component.page, self.classList['other']).pivot_cell()
    return self._css_pt_cell

  @property
  def cls_pt_axis(self):
    """
    Description:
    -----------

    :rtype: Classes.CatalogTable.CatalogTable
    """
    if self._css_pt_axis is None:
      self._css_pt_axis = Classes.CatalogTable.CatalogTable(
        self.component.page, self.classList['other']).pivot_axis()
    return self._css_pt_axis

  @property
  def cls_pt_filter_box(self):
    """
    Description:
    -----------

    :rtype: Classes.CatalogTable.CatalogTable
    """
    if self._css_pt_box is None:
      self._css_pt_box = Classes.CatalogTable.CatalogTable(
        self.component.page, self.classList['other']).pivot_filter_box()
    return self._css_pt_box

  @property
  def cls_pt_popup_header(self):
    """
    Description:
    -----------

    :rtype: Classes.CatalogTable.CatalogTable
    """
    if self._css_pt_pop_header is None:
      self._css_pt_pop_header = Classes.CatalogTable.CatalogTable(
        self.component.page, self.classList['other']).pivot_filter_popup_header()
    return self._css_pt_pop_header

  @property
  def cls_pt_popup_button(self):
    """
    Description:
    -----------

    :rtype: Classes.CatalogTable.CatalogTable
    """
    if self._css_pt_pop_button is None:
      self._css_pt_pop_button = Classes.CatalogTable.CatalogTable(
        self.component.page, self.classList['other']).pivot_filter_popup_button()
    return self._css_pt_pop_button

  @property
  def cls_pt_popup(self):
    """
    Description:
    -----------

    :rtype: Classes.CatalogTable.CatalogTable
    """
    if self._css_pt_pop is None:
      self._css_pt_pop = Classes.CatalogTable.CatalogTable(
        self.component.page, self.classList['other']).pivot_filter_popup()
    return self._css_pt_pop

  @property
  def cls_pt_val(self):
    """
    Description:
    -----------

    :rtype: Classes.CatalogTable.CatalogTable
    """
    if self._css_pt_val is None:
      self._css_pt_val = Classes.CatalogTable.CatalogTable(
        self.component.page, self.classList['other']).pivot_filter_val()
    return self._css_pt_val

  @property
  def cls_pt_label(self):
    """
    Description:
    -----------

    :rtype: Classes.CatalogTable.CatalogTable
    """
    if self._css_pt_label is None:
      self._css_pt_label = Classes.CatalogTable.CatalogTable(
        self.component.page, self.classList['other']).pivot_filter_label()
    return self._css_pt_label


class Aggrid(GrpCls.ClassHtml):

  def __init__(self, component):
    super(Aggrid, self).__init__(component)
    self.classList['main'].clear()
    self._css_head, self._css_row_even, self._css_row_odd, self._css_row = 4 * [None]
    self._css_cell_focus, self._css_cell, self._css_filter, self._css_menu, self._css_popup = 5 * [None]
    self.classList['other'].add(self.cls_head)
    self.classList['other'].add(self.cls_row_even)
    self.classList['other'].add(self.cls_row_odd)
    self.classList['other'].add(self.cls_row)
    self.classList['other'].add(self.cls_cell_focus)
    self.classList['other'].add(self.cls_cell)
    self.classList['other'].add(self.css_filter)
    self.classList['other'].add(self.css_menu)
    self.classList['other'].add(self.css_popup)

  @property
  def css_popup(self):
    """
    Description:
    ------------
    Property to the CSS Class definition for filter popups.

    :rtype: Classes.CatalogTable.CatalogTable
    """
    if self._css_popup is None:
      self._css_popup = Classes.CatalogTable.CatalogTable(
        self.component.page, self.classList['other']).ag_popup()
    return self._css_popup

  @property
  def css_menu(self):
    """
    Description:
    ------------
    Property to the CSS Class definition for menu.

    :rtype: Classes.CatalogTable.CatalogTable
    """
    if self._css_menu is None:
      self._css_menu = Classes.CatalogTable.CatalogTable(
        self.component.page, self.classList['other']).ag_menu()
    return self._css_menu

  @property
  def css_filter(self):
    """
    Description:
    ------------
    Property to the CSS Class definition for filter.

    :rtype: Classes.CatalogTable.CatalogTable
    """
    if self._css_filter is None:
      self._css_filter = Classes.CatalogTable.CatalogTable(
        self.component.page, self.classList['other']).ag_filter()
    return self._css_filter

  @property
  def cls_head(self):
    """
    Description:
    ------------
    Property to the CSS Class definition for header.

    :rtype: Classes.CatalogTable.CatalogTable
    """
    if self._css_head is None:
      self._css_head = Classes.CatalogTable.CatalogTable(
        self.component.page, self.classList['other']).ag_head()
    return self._css_head

  @property
  def cls_row_even(self):
    """
    Description:
    ------------
    Property to the CSS Class definition for rows.

    :rtype: Classes.CatalogTable.CatalogTable
    """
    if self._css_row_even is None:
      self._css_row_even = Classes.CatalogTable.CatalogTable(
        self.component.page, self.classList['other']).ag_row_even()
    return self._css_row_even

  @property
  def cls_row(self):
    """
    Description:
    ------------
    Property to the CSS Class definition for rows.

    :rtype: Classes.CatalogTable.CatalogTable
    """
    if self._css_row is None:
      self._css_row = Classes.CatalogTable.CatalogTable(
        self.component.page, self.classList['other']).ag_row()
    return self._css_row

  @property
  def cls_row_odd(self):
    """
    Description:
    ------------
    Property to the CSS Class definition for rows.

    :rtype: Classes.CatalogTable.CatalogTable
    """
    if self._css_row_odd is None:
      self._css_row_odd = Classes.CatalogTable.CatalogTable(
        self.component.page, self.classList['other']).ag_row_odd()
    return self._css_row_odd

  @property
  def cls_cell_focus(self):
    """
    Description:
    ------------
    Property to the CSS Class definition for cells when focus.

    :rtype: Classes.CatalogTable.CatalogTable
    """
    if self._css_cell_focus is None:
      self._css_cell_focus = Classes.CatalogTable.CatalogTable(
        self.component.page, self.classList['other']).ag_cell_focus()
    return self._css_cell_focus

  @property
  def cls_cell(self):
    """
    Description:
    ------------
    Property to the CSS Class definition for cells.

    :rtype: Classes.CatalogTable.CatalogTable
    """
    if self._css_cell is None:
      self._css_cell = Classes.CatalogTable.CatalogTable(
        self.component.page, self.classList['other']).ag_cell()
    return self._css_cell
