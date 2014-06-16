
#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
test_dj-twiml-views
------------

Tests for `dj-twiml-views` models module.
"""

import os
import shutil
import unittest
from django.test import TestCase

from dj_twiml.models import Twiml


class TestDj_twiml(TestCase):
    fixtures = ['dj_twiml.json']

    def setUp(self):
        self.snippets = Twiml.objects.all()

    def test_fields(self):
        for twiml in self.snippets:
            self.assertIs(type(twiml.name), unicode)
            self.assertIs(type(twiml.description), unicode)
            self.assertIs(type(twiml.content), unicode)

    def test_xml_conversion(self):
        t1 = self.snippets[0]
        self.assertEquals(t1.name, 'First twiml snippet')
        xml = t1.xml_view()
        self.assertEquals(
            '<?xml version="1.0" encoding="UTF-8"?><Response><Dial>+440123456789</Dial></Response>',
            xml)

    def tearDown(self):
        pass
