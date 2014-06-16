
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

from dj_twiml.models import Twiml


class TestDj_twiml(unittest.TestCase):

    def setUp(self):
        self.snippets = Twiml.objects.all()

    def test_fields(self):
        for twiml in self.snippets:
            self.assertIs(type(twiml.name), str)
            self.assertIs(type(twiml.description), str)
            self.assertIs(type(twiml.content), str)

    def tearDown(self):
        pass
