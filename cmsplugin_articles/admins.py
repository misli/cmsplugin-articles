from __future__ import absolute_import, division, generators, nested_scopes, print_function, unicode_literals, with_statement

from cms.admin.placeholderadmin import PlaceholderAdminMixin
from django.contrib import admin

from .utils import get_form


class ArticleAdmin(PlaceholderAdminMixin, admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}
    form = get_form('Article')

