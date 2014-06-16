
#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
test_dj-twiml-views
------------

Tests for `dj-twiml-views` views module.
"""

import os
import shutil
from django.test import TestCase

from dj_twiml import views


class TestDj_twiml(TestCase):
    fixtures = ['dj_twiml.json']

    def test_something(self):
        pass
