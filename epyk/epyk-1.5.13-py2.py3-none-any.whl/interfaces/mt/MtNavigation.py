#!/usr/bin/python
# -*- coding: utf-8 -*-

from epyk.fwk.mt.js import JsMdcComponents


class Navigation:

  def __init__(self, ui):
    self.page = ui.page

  def tabs(self, data, html_code=None):
    """
    Description:
    ------------
    Tabs organize and allow navigation between groups of content that are related and at the same level of hierarchy.
    The Tab Bar contains the Tab Scroller and Tab components.

    Related Pages:

      https://material.io/develop/web/components/tabs/tab-bar/

    Attributes:
    ----------
    :param data:
    :param html_code: Optional. String. The component identifier code (for both Python and Javascript)
    """
    schema = {"type": 'div', 'css': False, 'attrs': {'role': 'tablist'},
      'children': [
        {"type": 'div', 'css': False, 'class': 'mdc-tab-scroller', 'children': [
          {"type": 'div', 'css': False, 'class': "mdc-tab-scroller__scroll-area", 'children': [
            {"type": 'div', 'css': False, 'class': "mdc-tab-scroller__scroll-content", 'children': []}
          ]}
      ]}]
    }

    for text in data:
      schema['children'][0]['children'][0]['children'][0]['children'].append(
        {"type": 'button', 'css': False, 'class': 'mdc-tab mdc-tab--active', 'attrs': {"role": 'tab'},
         'arias': {"selected": False}, 'children': [
            {"type": 'div', 'css': False, 'class': 'mdc-tab__content', 'children': [
              {"type": 'span', 'css': False, 'class': 'mdc-tab__icon material-icons', 'arias': {"hidden": True}},
              {"type": 'span', 'css': False, 'class': 'mdc-tab__text-label', 'args': {"text": text}},
            ]},
             {"type": 'div', 'css': False, 'class': 'mdc-tab-indicator mdc-tab-indicator', 'children': [
               {"type": 'span', 'css': False, 'class': 'mdc-tab-indicator__content mdc-tab-indicator__content--underline'}]},
             {"type": 'span', 'css': False, 'class': 'mdc-tab__ripple'}]
         })

    html_t = self.page.web.mt.composite(schema, options={"reset_class": True})

    #
    dom_obj = JsMdcComponents.TabBar(html_t)
    html_t.style.builder(html_t.style.varName, dom_obj.instantiate("#%s" % html_t.htmlCode))
    # Add the specific dom features
    html_t.dom = dom_obj
    return html_t

  def top_bar(self, title, icon="menu", buttons=None, html_code=None):
    """
    Description:
    ------------
    MDC Top App Bar acts as a container for items such as application title, navigation icon, and action items.

    Related Pages:

      https://material.io/develop/web/components/tabs/tab-bar/

    Attributes:
    ----------
    :param title:
    :param icon:
    :param buttons:
    :param html_code: Optional. String. The component identifier code (for both Python and Javascript)
    """
    schema = {"type": 'header', 'css': False, 'children': [
                {"type": 'div', 'css': False, 'class': 'mdc-top-app-bar__row', 'children': [
                  {"type": 'section', 'css': False, 'class': "mdc-top-app-bar__section mdc-top-app-bar__section--align-start", 'children': [
                    {"type": 'icon', 'class-keep': True, 'css': False, 'args': {'text': icon}, 'class': "mdc-top-app-bar__navigation-icon mdc-icon-button"},
                    {"type": 'span', 'css': False, 'class': 'mdc-top-app-bar__title', 'args': {"text": title}},
                  ]},
                  {"type": 'div', 'css': False, 'class': 'mdc-top-app-bar__section mdc-top-app-bar__section--align-end', 'attrs': {"role": 'toolbar'}, 'children': []}
                ]}
    ]}

    if buttons is not None:
      for b in buttons:
        schema['children'][1]['children'].append(
          {"type": 'icon', 'class-keep': True, 'css': False, 'arias': {'label': b}, 'args': {'text': b}, 'class': "mdc-top-app-bar__navigation-icon mdc-icon-button"})
    html_t = self.page.web.mt.composite(schema, options={"reset_class": True})
    dom_obj = JsMdcComponents.TopBar(html_t)
    html_t.style.builder(html_t.style.varName, dom_obj.instantiate("#%s" % html_t.htmlCode))
    # Add the specific dom features
    html_t.dom = dom_obj
    return html_t

  def app_bar(self, title, icon="menu", buttons=None, html_code=None):
    """
    Description:
    ------------
    MDC Top App Bar acts as a container for items such as application title, navigation icon, and action items.

    Related Pages:

      https://material.io/develop/web/components/drawers/

    Attributes:
    ----------
    :param title:
    :param icon:
    :param buttons:
    :param html_code: Optional. String. The component identifier code (for both Python and Javascript)
    """
    schema = {"type": 'header', 'class-keep': True, 'class': 'app-bar', 'css': False, 'children': [
                {"type": 'div', 'css': False, 'class': 'mdc-top-app-bar__row', 'children': [
                  {"type": 'section', 'css': False, 'class': "mdc-top-app-bar__section mdc-top-app-bar__section--align-start", 'children': [
                    {"type": 'icon', 'class-keep': True, 'css': False, 'args': {'text': icon}, 'class': "mdc-top-app-bar__navigation-icon mdc-icon-button"},
                    {"type": 'span', 'css': False, 'class': 'mdc-top-app-bar__title', 'args': {"text": title}},
                  ]},
                  {"type": 'div', 'css': False, 'class': 'mdc-top-app-bar__section mdc-top-app-bar__section--align-end', 'attrs': {"role": 'toolbar'}, 'children': []}
                ]}
    ]}

    if buttons is not None:
      for b in buttons:
        schema['children'][1]['children'].append(
          {"type": 'icon', 'class-keep': True, 'css': False, 'arias': {'label': b}, 'args': {'text': b}, 'class': "mdc-top-app-bar__navigation-icon mdc-icon-button"})
    html_t = self.page.web.mt.composite(schema, options={"reset_class": True})
    dom_obj = JsMdcComponents.TopBar(html_t)
    html_t.style.builder(html_t.style.varName, dom_obj.instantiate("#%s" % html_t.htmlCode))
    # Add the specific dom features
    html_t.dom = dom_obj
    return html_t

  def drawers(self, sections, html_code=None):
    """
    Description:
    ------------
    The MDC Navigation Drawer is used to organize access to destinations and other functionality on an app.

    Related Pages:

      https://material.io/develop/web/components/drawers/

    Attributes:
    ----------
    :param sections:
    :param html_code: Optional. String. The component identifier code (for both Python and Javascript)
    """
    schema = {"type": 'aside', 'class-keep': True, 'class': 'mdc-drawer--modal', 'css': False, 'children': [
      {"type": 'div', 'css': False, 'class': 'mdc-drawer__content', 'children': [
        {"type": 'nav', 'class': 'mdc-list', 'css': False, 'children': []}]}
    ]}

    for s in sections:
      schema['children'][0]['children'][0]['children'].append(
        {"type": 'link', 'class': 'mdc-list-item', 'args': {"text": '', 'url': '#'}, 'css': False, 'children': [
          {"type": 'icon', 'class': 'material-icons mdc-list-item__graphic', 'css': False, 'arias': {'hidden': True}, 'args': {'text': 'inbox'}},
          {"type": 'span', 'css': False, 'class': 'mdc-list-item__text', 'args': {"text": s}}
        ]}
      )

    html_t = self.page.web.mt.composite(schema, options={"reset_class": True})
    dom_obj = JsMdcComponents.Drawers(html_t)
    html_t.style.builder(html_t.style.varName, dom_obj.instantiate("#%s" % html_t.htmlCode))
    # Add the specific dom features
    html_t.dom = dom_obj
    return html_t

  def drawer_app(self, text, html_code=None):
    """
    Description:
    ------------
    Apply the mdc-drawer-app-content class to the sibling element after the drawer for the open/close animations to work.

    Related Pages:

      https://material.io/develop/web/components/drawers/

    Attributes:
    ----------
    :param text:
    :param html_code: Optional. String. The component identifier code (for both Python and Javascript)
    """
    schema = {"type": 'div', 'class': 'mdc-drawer-scrim', 'args': {"components": text}}
    html_t = self.page.web.mt.composite(schema, options={"reset_class": True})
    #html_t.dom = dom_obj
    return html_t
