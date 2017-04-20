# -*- coding: utf-8 -*-
"""Module where all interfaces, events and exceptions live."""

from collective.facebook.instantarticles import _
from zope import schema
from zope.interface import Interface
from zope.publisher.interfaces.browser import IDefaultBrowserLayer


class IFacebookInstantarticlesLayer(IDefaultBrowserLayer):
    """Marker interface that defines a browser layer."""


class IInstantArticlesSettings(Interface):

    fb_page_codes = schema.List(
        title=_(
            'instantarticles_fbpagecodes_label',
            default=u'Facebook page codes'),
        description=_(
            'instantarticles_fbpagecodes_help',
            default=u'Insert a list of facebook page codes.'),
        value_type=schema.TextLine(),
        required=True,
        default=[]
    )
