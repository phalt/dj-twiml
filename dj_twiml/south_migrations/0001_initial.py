# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Twiml'
        db.create_table(u'dj_twiml_twiml', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('description', self.gf('django.db.models.fields.CharField')(max_length=100, blank=True)),
            ('content', self.gf('django.db.models.fields.TextField')(max_length=300)),
        ))
        db.send_create_signal(u'dj_twiml', ['Twiml'])


    def backwards(self, orm):
        # Deleting model 'Twiml'
        db.delete_table(u'dj_twiml_twiml')


    models = {
        u'dj_twiml.twiml': {
            'Meta': {'object_name': 'Twiml'},
            'content': ('django.db.models.fields.TextField', [], {'max_length': '300'}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        }
    }

    complete_apps = ['dj_twiml']