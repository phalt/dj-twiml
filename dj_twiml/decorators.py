# -*- coding: utf-8 -*-
from functools import wraps

from twilio.util import RequestValidator

from django.conf import settings

from django.views.decorators.csrf import csrf_exempt
from django.http import (
    HttpRequest, HttpResponse, HttpResponseForbidden, HttpResponseNotAllowed)

def twilio_secure_response(f):
    """ This decorator wraps plaintext Twilio TwiML responses and makes
        certain that the original HTTP request is from Twilio and that the
        HTTP response is correctly formatted.
    """
    @csrf_exempt
    @wraps(f)
    def decorator(request_or_self, methods=['POST'], *args, **kwargs):

        class_based_view = not(isinstance(request_or_self, HttpRequest))
        if not class_based_view:
            request = request_or_self
        else:
            assert len(args) >= 1
            request = args[0]

        # Turn off Twilio authentication when explicitly requested, or in debug mode.
        # Otherwise things do not work properly. For more information see the docs.
        use_forgery_protection = (
            getattr(settings,
                'DJANGO_TWILIO_FORGERY_PROTECTION',
                not settings.DEBUG))

        if use_forgery_protection:

            if request.method not in methods:
                return HttpResponseNotAllowed(request.method)

            # Forgery check
            t_auth_token = (getattr(
                            settings,
                            'TWILIO_AUTH_TOKEN',
                            'not settings.DEBUG')
                        )

            try:
                validator = RequestValidator(t_auth_token)
                url = request.build_absolute_uri()
                signature = request.META['HTTP_X_TWILIO_SIGNATURE']
            except (AttributeError, KeyError):
                return HttpResponseForbidden()

            if request.method == 'POST':
                if not validator.validate(url, request.POST, signature):
                    return HttpResponseForbidden()
            if request.method == 'GET':
                if not validator.validate(url, request.GET, signature):
                    return HttpResponseForbidden()

        response = f(request_or_self, *args, **kwargs)

        if isinstance(response, str):
            return HttpResponse(response, content_type='application/xml')
        else:
            return response
    return decorator
