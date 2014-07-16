# -*- coding: utf-8 -*-
from .models import Twiml
from .decorators import twilio_secure_response
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse


@twilio_secure_response
def detail(request, twiml_id):
    ''' Return the xml view for a twiml snippet '''
    twiml = Twiml.objects.get(id=twiml_id)
    return twiml.xml_view()
