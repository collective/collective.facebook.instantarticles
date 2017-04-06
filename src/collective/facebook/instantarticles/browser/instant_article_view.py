# -*- coding: utf-8 -*-
from plone import api
from Products.Five.browser import BrowserView


class View(BrowserView):
    '''
    View that formats item informations for instant articles
    '''

    def getImageTag(self):
        scales = api.content.get_view(
            name='images',
            context=self.context,
            request=self.request,
        )
        if not scales:
            return ""
        scale = scales.scale('image', scale="large")
        if not scale:
            return ""
        return scale.tag()

    def getFormattedDate(self, date):
        return date.strftime('%Y-%m-%dT%H:%M')

    def getCreator(self):
        creator = self.context.Creator()
        user = api.user.get(username=creator)
        if not user:
            return ""
        return user.getProperty('fullname') or creator

    def getText(self):
        """
        extract text from current content.
        AT and DX contents have different methods
        """
        try:
            return self.context.getText()
        except AttributeError:
            # DX content
            text = self.context.text
            if text:
                return text.output
        return ""
