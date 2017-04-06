# -*- coding: utf-8 -*-

from plone.app.layout.viewlets.common import ViewletBase
from plone import api
from collective.facebook.instantarticles.interfaces import IInstantArticlesSettings


class FacebookInstantArticlesViewlet(ViewletBase):

    def update(self):
        self.code = self.extractPageCodes()

    def extractPageCodes(self):
        codes = api.portal.get_registry_record(
            'fb_page_codes',
            interface=IInstantArticlesSettings)
        if not codes:
            return ''
        return (', ').join(codes)
