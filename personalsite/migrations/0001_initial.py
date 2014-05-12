# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Biography'
        db.create_table(u'personalsite_biography', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('text', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal(u'personalsite', ['Biography'])

        # Adding model 'Event'
        db.create_table(u'personalsite_event', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('event_date', self.gf('django.db.models.fields.TextField')()),
            ('event_description', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal(u'personalsite', ['Event'])

        # Adding model 'Media'
        db.create_table(u'personalsite_media', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('media_text', self.gf('django.db.models.fields.TextField')()),
            ('media_description', self.gf('django.db.models.fields.TextField')()),
            ('media_type', self.gf('django.db.models.fields.CharField')(default='VI', max_length=2)),
        ))
        db.send_create_signal(u'personalsite', ['Media'])


    def backwards(self, orm):
        # Deleting model 'Biography'
        db.delete_table(u'personalsite_biography')

        # Deleting model 'Event'
        db.delete_table(u'personalsite_event')

        # Deleting model 'Media'
        db.delete_table(u'personalsite_media')


    models = {
        u'personalsite.biography': {
            'Meta': {'object_name': 'Biography'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'text': ('django.db.models.fields.TextField', [], {})
        },
        u'personalsite.event': {
            'Meta': {'object_name': 'Event'},
            'event_date': ('django.db.models.fields.TextField', [], {}),
            'event_description': ('django.db.models.fields.TextField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'personalsite.media': {
            'Meta': {'object_name': 'Media'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'media_description': ('django.db.models.fields.TextField', [], {}),
            'media_text': ('django.db.models.fields.TextField', [], {}),
            'media_type': ('django.db.models.fields.CharField', [], {'default': "'VI'", 'max_length': '2'})
        }
    }

    complete_apps = ['personalsite']