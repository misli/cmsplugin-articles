# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Article'
        db.create_table(u'cmsplugin_articles_article', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('polymorphic_ctype', self.gf('django.db.models.fields.related.ForeignKey')(related_name=u'polymorphic_cmsplugin_articles.article_set', null=True, to=orm['contenttypes.ContentType'])),
            ('namespace', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=250)),
            ('slug', self.gf('django.db.models.fields.SlugField')(max_length=250)),
            ('pub_date', self.gf('django.db.models.fields.DateField')()),
            ('perex', self.gf('djangocms_text_ckeditor.fields.HTMLField')(default=u'', blank=True)),
            ('text', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['cms.Placeholder'], null=True)),
            ('page_title', self.gf('django.db.models.fields.CharField')(max_length=250, null=True, blank=True)),
            ('menu_title', self.gf('django.db.models.fields.CharField')(max_length=250, null=True, blank=True)),
            ('meta_desc', self.gf('django.db.models.fields.TextField')(default=u'', blank=True)),
            ('public', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal(u'cmsplugin_articles', ['Article'])

        # Adding unique constraint on 'Article', fields ['pub_date', 'slug']
        db.create_unique(u'cmsplugin_articles_article', ['pub_date', 'slug'])


    def backwards(self, orm):
        # Removing unique constraint on 'Article', fields ['pub_date', 'slug']
        db.delete_unique(u'cmsplugin_articles_article', ['pub_date', 'slug'])

        # Deleting model 'Article'
        db.delete_table(u'cmsplugin_articles_article')


    models = {
        'cms.placeholder': {
            'Meta': {'object_name': 'Placeholder'},
            'default_width': ('django.db.models.fields.PositiveSmallIntegerField', [], {'null': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'slot': ('django.db.models.fields.CharField', [], {'max_length': '50', 'db_index': 'True'})
        },
        u'cmsplugin_articles.article': {
            'Meta': {'unique_together': "[(u'pub_date', u'slug')]", 'object_name': 'Article'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'menu_title': ('django.db.models.fields.CharField', [], {'max_length': '250', 'null': 'True', 'blank': 'True'}),
            'meta_desc': ('django.db.models.fields.TextField', [], {'default': "u''", 'blank': 'True'}),
            'namespace': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'page_title': ('django.db.models.fields.CharField', [], {'max_length': '250', 'null': 'True', 'blank': 'True'}),
            'perex': ('djangocms_text_ckeditor.fields.HTMLField', [], {'default': "u''", 'blank': 'True'}),
            'polymorphic_ctype': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "u'polymorphic_cmsplugin_articles.article_set'", 'null': 'True', 'to': u"orm['contenttypes.ContentType']"}),
            'pub_date': ('django.db.models.fields.DateField', [], {}),
            'public': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '250'}),
            'text': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['cms.Placeholder']", 'null': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '250'})
        },
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        }
    }

    complete_apps = ['cmsplugin_articles']