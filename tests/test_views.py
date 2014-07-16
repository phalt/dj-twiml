
#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
test_dj-twiml-views
------------

Tests for `dj-twiml-views` views module.
"""

from hmac import new
from hashlib import sha1
from base64 import encodestring


import os
import shutil
from django.test import Client, TestCase, RequestFactory

from django_twilio import settings

from dj_twiml import views, models


class TestDj_twiml(TestCase):
    fixtures = ['dj_twiml.json']

    def setUp(self):
        self.client = Client()
        self.factory = RequestFactory()

        self.uri = 'http://testserver/twiml/'
        self.t1_uri = '/twiml/1/'

        settings.TWILIO_ACCOUNT_SID = 'xxx'
        settings.TWILIO_AUTH_TOKEN = 'xxx'

        self.signature = encodestring(
            new(settings.TWILIO_AUTH_TOKEN,
                '%s/1/' % self.uri, sha1).digest()).strip()

    def test_detail(self):
        request = self.factory.post(
            self.t1_uri, HTTP_X_TWILIO_SIGNATURE=self.signature)
        deets = views.detail(request, twiml_id=1)

        self.assertEquals(deets.status_code, 200)
        self.assertEquals(
            deets._headers['content-type'],
            ('Content-Type', 'text/xml')
        )
        self.assertEquals(
            deets._container,
            [u'<?xml version="1.0" encoding="UTF-8"?><Response><Dial>+440123456789</Dial></Response>']
        )

