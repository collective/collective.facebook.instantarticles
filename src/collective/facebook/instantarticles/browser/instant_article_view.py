# -*- coding: utf-8 -*-
from lxml import etree
from lxml import html
from plone import api
from Products.Five.browser import BrowserView


class View(BrowserView):
    """
    View that formats item informations for instant articles
    """

    def getImageTag(self):
        scales = api.content.get_view(
            name='images',
            context=self.context,
            request=self.request,
        )
        if not scales:
            return ''
        scale = scales.scale('image', scale='large')
        if not scale:
            return ''
        return scale.tag()

    def getFormattedDate(self, date):
        return date.strftime('%Y-%m-%dT%H:%M')

    def getCreator(self):
        creator = self.context.Creator()
        user = api.user.get(username=creator)
        if not user:
            return ''
        return user.getProperty('fullname') or creator

    def getText(self):
        """"
        extract text from current content.
        AT and DX contents have different methods
        """
        text = ''
        try:
            text = self.context.getText()
        except AttributeError:
            # DX content
            field = getattr(self.context, 'text', None)
            if field:
                text = field.output
        if not text:
            return ''
        return self.fixText(text)

    def fixText(self, text):
        """
        Tiny insert images inside the current <p> tag, but Facebook wrap
        images in a <figure> tag that can't be inside a <p>, so we need to move
        the image outside it's container.
        """
        if not isinstance(text, unicode):
            text = text.decode('utf-8')
        tree = html.fragment_fromstring(text, create_parent=True)
        images = tree.xpath('//img')
        for image in images:
            paragraph = image.getparent()
            # remove the image from its parent
            etree.strip_elements(paragraph, 'img',  with_tail=False)
            pContainer = paragraph.getparent()
            pIndex = pContainer.index(paragraph)
            pContainer.insert(pIndex, image)
        return etree.tostring(tree, encoding='utf-8', method='html')
