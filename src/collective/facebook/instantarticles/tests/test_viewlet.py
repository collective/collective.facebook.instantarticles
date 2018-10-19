# -*- coding: utf-8 -*-
"""Viewlet tests for this package."""
from collective.facebook.instantarticles.browser.viewlets import FacebookInstantArticlesViewlet  # NOQA
from collective.facebook.instantarticles.interfaces import IInstantArticlesSettings  # NOQA
from collective.facebook.instantarticles.testing import COLLECTIVE_FACEBOOK_INSTANTARTICLES_INTEGRATION_TESTING  # NOQA
from plone import api

import unittest


class TestViewlet(unittest.TestCase):
    """
    Test that collective.facebook.instantarticles properly render the viewlet
    with given code.
    """

    layer = COLLECTIVE_FACEBOOK_INSTANTARTICLES_INTEGRATION_TESTING

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer['portal']
        self.request = self.portal.REQUEST

    def test_viewlet_notrendered_without_settings(self):
        viewlet = FacebookInstantArticlesViewlet(
            self.portal,
            self.request,
            None,
            None)
        viewlet.update()
        self.assertEqual(viewlet.code, '')
        self.assertEqual(viewlet.extractPageCodes(), '')
        self.assertFalse('fb:pages' in self.portal.view())

    def test_viewlet_rendered_with_one_code(self):
        code = u'foo'
        meta = '<meta property="fb:pages" content="{0}" />'.format(code)
        api.portal.set_registry_record(
            'fb_page_codes',
            [code, ],
            interface=IInstantArticlesSettings
        )
        viewlet = FacebookInstantArticlesViewlet(
            self.portal,
            self.request,
            None,
            None)
        viewlet.update()
        self.assertEqual(viewlet.code, code)
        self.assertEqual(viewlet.extractPageCodes(), code)
        self.assertTrue('fb:pages' in self.portal.view())
        self.assertTrue(meta in self.portal.view())

    def test_viewlet_rendered_with_two_codes(self):
        codes = [u'foo', u'bar']
        str_codes = ', '.join(codes)
        meta = '<meta property="fb:pages" content="{0}" />'.format(str_codes)
        api.portal.set_registry_record(
            'fb_page_codes',
            codes,
            interface=IInstantArticlesSettings
        )
        viewlet = FacebookInstantArticlesViewlet(
            self.portal,
            self.request,
            None,
            None)
        viewlet.update()
        self.assertEqual(viewlet.code, str_codes)
        self.assertEqual(viewlet.extractPageCodes(), str_codes)
        self.assertTrue('fb:pages' in self.portal.view())
        self.assertTrue(meta in self.portal.view())
