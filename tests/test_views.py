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


from django.test import Client, TestCase, RequestFactory

from django.conf import settings

from dj_twiml import views


class TestDj_twiml(TestCase):
    fixtures = ['dj_twiml.json']

    def setUp(self):
        self.client = Client()
        self.factory = RequestFactory()

        self.uri = 'http://testserver/twiml/'
        self.t1_uri = '/twiml/1/'

        settings.TWILIO_AUTH_TOKEN = 'xxx'
        settings.TWILIO_ACCOUNT_SID = 'xxx'

        self.signature = encodestring(
            new(settings.TWILIO_AUTH_TOKEN,
                '%s1/' % self.uri, sha1).digest()).strip()

    def test_detail_forgery_off(self):
        request = self.factory.post(
            self.t1_uri, HTTP_X_TWILIO_SIGNATURE=self.signature)
        deets = views.detail(request, twiml_id=1)

        self.assertIn('<Response><Dial>', deets)

    def test_detail_forgery_on(self):
        ''' Same as above but with forgery protection on'''
        settings.DJANGO_TWILIO_FORGERY_PROTECTION = True
        request = self.factory.post(
            self.t1_uri, HTTP_X_TWILIO_SIGNATURE=self.signature)
        deets = views.detail(request, twiml_id=1)

        self.assertIn('<Response><Dial>', deets)
