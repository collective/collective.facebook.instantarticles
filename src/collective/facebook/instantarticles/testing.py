# -*- coding: utf-8 -*-
from plone.app.contenttypes.testing import PLONE_APP_CONTENTTYPES_FIXTURE
from plone.app.testing import applyProfile
from plone.app.testing import FunctionalTesting
from plone.app.testing import IntegrationTesting
from plone.app.testing import PloneSandboxLayer

import collective.facebook.instantarticles


class CollectiveFacebookInstantarticlesLayer(PloneSandboxLayer):

    defaultBases = (PLONE_APP_CONTENTTYPES_FIXTURE,)

    def setUpZope(self, app, configurationContext):
        # Load any other ZCML that is required for your tests.
        # The z3c.autoinclude feature is disabled in the Plone fixture base
        # layer.
        self.loadZCML(package=collective.facebook.instantarticles)

    def setUpPloneSite(self, portal):
        applyProfile(portal, 'collective.facebook.instantarticles:default')


COLLECTIVE_FACEBOOK_INSTANTARTICLES_FIXTURE = (
    CollectiveFacebookInstantarticlesLayer()
)


COLLECTIVE_FACEBOOK_INSTANTARTICLES_INTEGRATION_TESTING = IntegrationTesting(
    bases=(COLLECTIVE_FACEBOOK_INSTANTARTICLES_FIXTURE,),
    name='CollectiveFacebookInstantarticlesLayer:IntegrationTesting',
)


COLLECTIVE_FACEBOOK_INSTANTARTICLES_FUNCTIONAL_TESTING = FunctionalTesting(
    bases=(COLLECTIVE_FACEBOOK_INSTANTARTICLES_FIXTURE,),
    name='CollectiveFacebookInstantarticlesLayer:FunctionalTesting',
