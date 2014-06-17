# -*- coding: utf-8 -*-
from django.db import models
from twilio.twiml import TwimlException
from xml.etree import ElementTree as ET


class Twiml(models.Model):

    def __unicode__(self):
        return self.name

    name = models.CharField(max_length=100)

    description = models.CharField(max_length=100, blank=True)

    content = models.TextField(max_length=300)

    def xml_view(self):
            ''' Return the xml-ified version of the content.

                An XML validation is also performed and will return an
                XML error if the content is not formatted correctly.
            '''
            try:
                ET.fromstring(self.content)
            except:
                raise TwimlException
            return '<?xml version="1.0" encoding="UTF-8"?>' + self.content
