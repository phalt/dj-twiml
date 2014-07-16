==============
dj-twiml-views
==============

.. image:: https://badge.fury.io/py/dj-twiml-views.png
    :target: http://badge.fury.io/py/dj-twiml-views

.. image:: https://pypip.in/d/dj-twiml-views/badge.png
    :target: https://crate.io/packages/dj-twiml-views?version=latest


Create static Twilio TwiML views in Django

About
-----

Often when building Twilio apps with Django, you want to quickly create a few simple static TwiML documents. You can usually do this by writing some code and linking it to a URL endpoint on your Django app.

But what if you wanted to modify those documents? Or perhaps you don't have the means to push the updates to the live server straight away?

dj-twiml-views lets you create and modify **static** TwiML documents in seconds, with a publicly addressable URL and correct XML formatting / validation.

This is perfect if you want static TwiML documents that do not require any computation, but might need modifying occassionally.

Installation
------------

Install dj-twiml-views::

    pip install dj-twiml

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

Usage
-----

1. Create a new TwiML document through the admin panel (/admin/dj_twiml/twiml/)

.. image:: http://i.imgur.com/rPRjptp.png

2. Save it and test it out by sending a HTTP POST request to the new URL. The __unicode__ name of the object will show the URL:

.. image:: http://i.imgur.com/kA6hVYR.png

3. Point a Twilio phone number to the new dj-twiml snippet

.. image:: http://i.imgur.com/YIzeZR3.png

4. Ring it! Try calling **++442030952720** (UK) or **+1 844-707-9437** (USA) now :)


Features
--------

* Quickly build new or modify existing static TwiML snippets.
