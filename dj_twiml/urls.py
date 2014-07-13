# -*- coding: utf-8 -*-
from django.conf.urls import patterns, url
import views

urlpatterns = patterns(
    '',
    url(r'^(?P<twiml_id>\d+)/$', views.detail, name='detail'),
)
