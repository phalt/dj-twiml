# -*- coding: utf-8 -*-
from .models import Twiml
from django_twilio.decorators import twilio_view

@twilio_view
def detail(request, twiml_id):
    ''' Return the xml view for a twiml snippet '''
    twiml = Twiml.objects.get(id=twiml_id)
    return twiml.xml_view()
