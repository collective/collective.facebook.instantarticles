.. This README is meant for consumption by humans and pypi. Pypi can render rst files so please do not use Sphinx features.
   If you want to learn more about writing documentation, please check out: http://docs.plone.org/about/documentation_styleguide.html
   This text does not appear on pypi or github. It is a comment.

==============================================================================
collective.facebook.instantarticles
==============================================================================

.. image:: https://travis-ci.org/collective/collective.facebook.instantarticles.svg?branch=master
    :target: https://travis-ci.org/collective/collective.facebook.instantarticles

Plone integration for Facebook Instant Articles.

If you don't know them, instant articles are a new way to publish/read contents in
Facebook pages with mobile devices.

There are two ways to populate instant articles: with javascript api or with an
RSS feed. This product handle the second option.

For more references, go to `official page <https://instantarticles.fb.com>`_.

Features
--------

- Controlpanel to setup a list of FB pages ids
- Viewlet that expose a meta-tag with the list of ids
- *fb.rss* collection view that formats collection results to be parsed by Facebook
- *instant_article* view that format single content infos with a set of standards needed by Facebook.


Translations
------------

This product has been translated into

- English
- Italian


Installation
------------

Install collective.facebook.instantarticles by adding it to your buildout::

    [buildout]

    ...

    eggs =
        collective.facebook.instantarticles


and then running ``bin/buildout``


RSS view
--------

In Facebook page's Instant Articles settings, you need to insert an address where
it can retrieve an RSS feed to populate the list of pending articles.
This feed needs some custom tags and infos, so we created a specific view for this purpose.

There is a new view registered for Collections: 'fb.rss' that format informations
in the correct way, so in Instant Articles config you need to insert an url like this:

``http://your_site_url/collection-for-facebook/fb.rss``

instant_article view
--------------------

The RSS view needs to expose all relevant informations for each result item.

This is done with a view called ``instant_article`` that can be called over an object,
and returns a formatted html with some generic informations.
If you want to expose different informations for a specific content-type, you only need
to override this view for the desired content-type.


Instant Articles provides several ways to format texts, images and videos
(see the `docs <https://developers.facebook.com/docs/instant-articles>`_), so we register a generic view that covers a simple use-case
(documents and news with images for example), but if you need a specific format
for your custom content-type, you only need to register an 'instant_article' view
for it.

Contribute
----------

- Issue Tracker: https://github.com/collective/collective.facebook.instantarticles/issues
- Source Code: https://github.com/collective/collective.facebook.instantarticles


License
-------

The project is licensed under the GPLv2.

Credits
=======

Developed with the support of:

* `Regione Emilia Romagna`__

Regione Emilia Romagna supports the `PloneGov initiative`__.

__ http://www.regione.emilia-romagna.it/
__ http://www.plonegov.it/
