# -*- coding: utf-8 -*-
"""Setup tests for this package."""
from collective.facebook.instantarticles.testing import COLLECTIVE_FACEBOOK_INSTANTARTICLES_INTEGRATION_TESTING  # NOQA
from plone import api

import unittest


class TestSetup(unittest.TestCase):
    """Test that collective.facebook.instantarticles is properly installed."""

    layer = COLLECTIVE_FACEBOOK_INSTANTARTICLES_INTEGRATION_TESTING

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer['portal']
        self.installer = api.portal.get_tool('portal_quickinstaller')

    def test_product_installed(self):
        """Test if collective.facebook.instantarticles is installed."""
        self.assertTrue(self.installer.isProductInstalled(
            'collective.facebook.instantarticles'))

    def test_browserlayer(self):
        """Test that IFacebookInstantarticlesLayer is registered."""
        from collective.facebook.instantarticles.interfaces import (
            IFacebookInstantarticlesLayer)
        from plone.browserlayer import utils
        self.assertIn(IFacebookInstantarticlesLayer, utils.registered_layers())


class TestUninstall(unittest.TestCase):

    layer = COLLECTIVE_FACEBOOK_INSTANTARTICLES_INTEGRATION_TESTING

    def setUp(self):
        self.portal = self.layer['portal']
        self.installer = api.portal.get_tool('portal_quickinstaller')
        self.installer.uninstallProducts(
            ['collective.facebook.instantarticles']
        )

    def test_product_uninstalled(self):
        """
        Test if collective.facebook.instantarticles is cleanly uninstalled.
        """
        self.assertFalse(self.installer.isProductInstalled(
            'collective.facebook.instantarticles'))

    def test_browserlayer_removed(self):
        """
        Test that IFacebookInstantarticlesLayer is removed.
        """
        from collective.facebook.instantarticles.interfaces import \
            IFacebookInstantarticlesLayer
        from plone.browserlayer import utils
        self.assertNotIn(
            IFacebookInstantarticlesLayer,
            utils.registered_layers()
        )
