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

Often when building [Twilio TwiML views][1], you want to quickly create a few simple static TwiML documents. You can do this by writing some code and linking it to a URL endpoint on your Django app.

But what if you wanted to modify the document? Or perhaps you don't have the means to push the updates to the live server straight away?

dj-twiml-views lets you create and modify __static__ TwiML documents in seconds, with a publicly addressable URL and correct XML formatting / validation.


Documentation
-------------

The full documentation is at http://dj-twiml-views.rtfd.org.

Quickstart
----------

Install dj-twiml-views::

    pip install dj-twiml-views

Then use it in a project::

    import dj-twiml-views

Features
--------

* Quickly build new or modify existing static TwiML snippets.

* TODO


[1]: https://www.twilio.com/docs/api/twiml
