# -*- coding: utf-8 -*-

from plone import api
from plone.subrequest import subrequest
from Products.Five.browser import BrowserView


class View(BrowserView):
    '''
    RSS view for Facebook instant articles
    '''

    def __call__(self):
        self.request.response.setHeader('Content-Type',
                                        'application/atom+xml')
        return self.index()

    def get_current_language(self):
        return api.portal.get_current_language()

    def get_item_html(self, item):
        response = subrequest(item.getURL() + '?ajax_load=1')
        return response.getBody()
