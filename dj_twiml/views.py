# -*- coding: utf-8 -*-
from .models import Twiml
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse


@csrf_exempt
def detail(request, twiml_id):
    ''' Return the xml view for a twiml snippet '''
    twiml = Twiml.objects.get(id=twiml_id)
    return HttpResponse(twiml.xml_view(), content_type='text/xml')
