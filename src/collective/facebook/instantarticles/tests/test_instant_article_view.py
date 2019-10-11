# -*- coding: utf-8 -*-
"""Viewlet tests for this package."""
from collective.facebook.instantarticles.browser.viewlets import (
    FacebookInstantArticlesViewlet,
)  # NOQA
from collective.facebook.instantarticles.interfaces import (
    IInstantArticlesSettings,
)  # NOQA
from collective.facebook.instantarticles.testing import (
    COLLECTIVE_FACEBOOK_INSTANTARTICLES_INTEGRATION_TESTING,
)  # NOQA
from plone import api

import unittest


class TestInstantArticleView(unittest.TestCase):
    """
    Test support view
    """

    layer = COLLECTIVE_FACEBOOK_INSTANTARTICLES_INTEGRATION_TESTING

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer['portal']
        self.request = self.portal.REQUEST

    def testFixText(self):
        view = api.content.get_view(
            name='instant_article', context=self.portal, request=self.request
        )
        img_tag = '<img src="something" />'
        img_inside_p = '<p><img src="something" /> Example.</p>'
        self.assertEqual(
            view.fixText(img_tag), '<div><img src="something"></div>'
        )
        self.assertEqual(
            view.fixText(img_inside_p),
            '<div><img src="something"><p> Example.</p></div>',
        )

