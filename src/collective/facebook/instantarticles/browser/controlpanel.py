# -*- coding: utf-8 -*-
from collective.facebook.instantarticles import _
from collective.facebook.instantarticles.interfaces import IInstantArticlesSettings # NOQA
from plone.app.registry.browser.controlpanel import ControlPanelFormWrapper
from plone.app.registry.browser.controlpanel import RegistryEditForm


class InstantArticlesSettingsEditForm(RegistryEditForm):
    """settings form."""
    schema = IInstantArticlesSettings
    id = 'InstantArticlesSettingsEditForm'
    label = _(u'Facebook instant articles settings')
    description = u''

    def updateWidgets(self):
        """
        Set more visible rows
        """
        super(InstantArticlesSettingsEditForm, self).updateWidgets()
        self.widgets['fb_page_codes'].rows = 7


class InstantArticlesSettingsControlPanel(ControlPanelFormWrapper):
    """settings control panel.
    """
    form = InstantArticlesSettingsEditForm
