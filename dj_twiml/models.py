# -*- coding: utf-8 -*-
from django.db import models


class Twiml(models.Model):

    def __unicode__(self):
        return self.name

    name = models.CharField(max_length=100)

    description = models.CharField(max_length=100, blank=True)

    content = models.TextField(max_length=300)

