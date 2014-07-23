# DJ-TWIML

![PyPI version](https://badge.fury.io/py/dj-twiml.png)
![Downloads](https://pypip.in/d/dj-twiml/badge.png)

Create and modify static Twilio TwiML views in Django

## About

Often when building [Twilio](https://twilio.com) apps with Django, you want to quickly create a few simple static [TwiML](https://twilio.com/docs/api/twiml) documents. You can usually do this by writing a view and connecting it to a URL endpoint on your Django app.

But what if you wanted to modify those documents quickly later on? Or perhaps you don't have the means to push the updates to the live server straight away?

dj-twiml lets you create and modify **static** TwiML documents in seconds, with a publicly addressable URL and correct XML formatting / validation.

This is perfect if you want static TwiML documents that do not require any computation, but might need modifying occassionally.

## Installation

* Install dj-twiml

```
    $ pip install dj-twiml
```

* Add dj-twiml and django-twilio to your installed apps in settings. Add the settings for django-twilio.

```
    INSTALLED_APPS = (
        ...,
        'django_twilio',
        'dj_twiml',
    )

    TWILIO_ACCOUNT_SID='ACXXXXXXXXXXXXXXXXXX'
    TWILIO_AUTH_TOKEN='ATXXXXXXXXXXXXXXXXXX'

    # Set this to True in production
    DJANGO_TWILIO_FORGERY_PROTECTION = False
```

* Dj-twiml will install [django_twilio](http://django-twilio.readthedocs.org/en/latest/install.html#installation) for you, but you will also need to follow the django-twilio [installation instructions](http://django-twilio.readthedocs.org/en/latest/install.html#installation) too.

* After setting up django-twilio, add the URL routing to your URLconf (urls.py)::

```
    urlpatterns = patterns(
        '',
        url(r'twiml/', include('dj_twiml.urls')),
        ...
    )
```

Finally, you can run the following command on Django 1.7 and Django 1.6 (with South installed) to setup the dj_twiml database models:

```
    $ python manage.py migrate dj_twiml
```

## Usage

1. Create a new TwiML document through the admin panel (/admin/dj_twiml/twiml/)

![Django admin panel](http://i.imgur.com/rPRjptp.png)

2. Save it and test it out by sending a HTTP POST request to the new URL. The __unicode__ name of the object will show the URL:

![TwiML output](http://i.imgur.com/kA6hVYR.png)

3. Point a Twilio phone number to the new dj-twiml snippet:

![Twilio phone number page](http://i.imgur.com/YIzeZR3.png)

(Get a new [Twilio trial account](https://twilio.com/try-twilio) here.)

4. Ring it! Try calling **++442030952720** (UK) or **+1 844-707-9437** (USA) now :)


Features
--------

* Quickly build new or modify existing static TwiML snippets.

* Supports both Django 1.7 and Django 1.6

* Built on top of [django_twilio](https://github.com/rdegges/django-twilio).
