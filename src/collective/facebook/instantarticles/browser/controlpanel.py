# -*- coding: utf-8 -*-
from plone.app.registry.browser.controlpanel import RegistryEditForm
from plone.app.registry.browser.controlpanel import ControlPanelFormWrapper
from collective.facebook.instantarticles.interfaces import IInstantArticlesSettings
from collective.facebook.instantarticles import _


class InstantArticlesSettingsEditForm(RegistryEditForm):
    """settings form."""
    schema = IInstantArticlesSettings
    id = "InstantArticlesSettingsEditForm"
    label = _(u"Facebook instant articles settings")
    description = u""


class InstantArticlesSettingsControlPanel(ControlPanelFormWrapper):
    """settings control panel.
    """
    form = InstantArticlesSettingsEditForm
