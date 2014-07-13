=============================
dj-twiml-views
=============================

.. image:: https://badge.fury.io/py/dj-twiml-views.png
    :target: http://badge.fury.io/py/dj-twiml-views

.. image:: https://travis-ci.org/phalt/dj-twiml-views.png?branch=master
    :target: https://travis-ci.org/phalt/dj-twiml-views

.. image:: https://coveralls.io/repos/phalt/dj-twiml-views/badge.png?branch=master
    :target: https://coveralls.io/r/phalt/dj-twiml-views?branch=master

.. image:: https://pypip.in/d/dj-twiml-views/badge.png
    :target: https://crate.io/packages/dj-twiml-views?version=latest


Create static Twilio TwiML views in Django

About
-----

Often when building Twilio apps with Django, you want to quickly create a few simple static TwiML documents. You can usually do this by writing some code and linking it to a URL endpoint on your Django app.

But what if you wanted to modify those documents? Or perhaps you don't have the means to push the updates to the live server straight away?

dj-twiml-views lets you create and modify **static** TwiML documents in seconds, with a publicly addressable URL and correct XML formatting / validation.

This is perfect if you have TwiML documents that do not require any computation, but
might need modifying occassionally.


Documentation
-------------

The full documentation is at http://dj-twiml-views.rtfd.org.

Quickstart
----------

Install dj-twiml-views::

    pip install dj-twiml

Then use it in a project::

    import dj-twiml

Add dj-twiml to your installed apps::

    INSTALLED_APPS = {
        ...,
        'dj_twiml',
    }

and to your URLconf (urls.py)::

    urlpatterns = patterns(
        '',
        url(r'^$', include('dj_twiml.urls')),
        ...
    )

and finally set things up using South::

    $ python manage.py migrate dj_twiml


Features
--------

* Quickly build new or modify existing static TwiML snippets.
