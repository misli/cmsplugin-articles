# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import cms.models.fields
import djangocms_text_ckeditor.fields


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0003_auto_20140926_2347'),
        ('contenttypes', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('namespace', models.CharField(max_length=200, verbose_name='Application instance')),
                ('title', models.CharField(max_length=250, verbose_name='Title')),
                ('slug', models.SlugField(max_length=250, verbose_name='Slug')),
                ('pub_date', models.DateField(verbose_name='Publication date')),
                ('perex', djangocms_text_ckeditor.fields.HTMLField(default='', verbose_name='Perex', blank=True)),
                ('page_title', models.CharField(help_text='Overwrite the title (html title tag)', max_length=250, null=True, verbose_name='Page title', blank=True)),
                ('menu_title', models.CharField(help_text='Overwrite the title in the menu', max_length=250, null=True, verbose_name='Menu title', blank=True)),
                ('meta_desc', models.TextField(default='', help_text='The text displayed in search engines.', verbose_name='Meta description', blank=True)),
                ('public', models.BooleanField(default=False, verbose_name='Public')),
                ('polymorphic_ctype', models.ForeignKey(related_name='polymorphic_cmsplugin_articles.article_set', editable=False, to='contenttypes.ContentType', null=True)),
                ('text', cms.models.fields.PlaceholderField(slotname='article_text', editable=False, to='cms.Placeholder', null=True)),
            ],
            options={
                'ordering': ('-pub_date',),
                'verbose_name': 'Article',
                'verbose_name_plural': 'Articles',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ArticlePlugin',
            fields=[
                ('cmsplugin_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='cms.CMSPlugin')),
                ('template', models.CharField(default='default', help_text='The template used to render plugin.', max_length=100, verbose_name='Template', choices=[('default', 'Default')])),
                ('article', models.ForeignKey(verbose_name='Article', to='cmsplugin_articles.Article')),
            ],
            options={
                'abstract': False,
            },
            bases=('cms.cmsplugin',),
        ),
        migrations.CreateModel(
            name='LastArticlesPlugin',
            fields=[
                ('cmsplugin_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='cms.CMSPlugin')),
                ('number', models.IntegerField(default=3, verbose_name='Number of last articles')),
                ('template', models.CharField(default='default', help_text='The template used to render plugin.', max_length=100, verbose_name='Template', choices=[('default', 'Default')])),
            ],
            options={
                'abstract': False,
            },
            bases=('cms.cmsplugin',),
        ),
        migrations.AlterUniqueTogether(
            name='article',
            unique_together=set([('pub_date', 'slug')]),
        ),
    ]
