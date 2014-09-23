from __future__ import absolute_import, division, generators, nested_scopes, print_function, unicode_literals, with_statement

from django.conf import settings
from django.conf.urls import patterns, url

from .utils import get_view


articles = patterns('',
    url(r'^$',                                                                      get_view('index'),  name='index'),
    url(r'^(?P<year>[0-9]{4})/$',                                                   get_view('year'),   name='year'),
    url(r'^(?P<year>[0-9]{4})/(?P<month>[0-9]+)/$',                                 get_view('month'),  name='month'),
    url(r'^(?P<year>[0-9]{4})/(?P<month>[0-9]+)/(?P<day>[0-9]+)/$',                 get_view('day'),    name='day'),
    url(r'^(?P<year>[0-9]{4})/(?P<month>[0-9]+)/(?P<day>[0-9]+)/(?P<slug>[^/]+)/$', get_view('detail'), name='detail'),
)

