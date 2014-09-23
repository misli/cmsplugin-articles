# -*- coding: utf-8 -*-

from __future__ import absolute_import, division, generators, nested_scopes, print_function, unicode_literals, with_statement

from django.utils.translation import ugettext_lazy as _

from cms.app_base import CMSApp
from cms.apphook_pool import apphook_pool
from .urls import articles


@apphook_pool.register
class ArticlesApp(CMSApp):
    name     = _('Articles')
    urls     = [articles]
    app_name = 'Articles'


