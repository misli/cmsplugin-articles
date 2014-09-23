from __future__ import unicode_literals

from cms.admin.placeholderadmin import PlaceholderAdminMixin
from django.contrib import admin

from .utils import get_form


class ArticleAdmin(PlaceholderAdminMixin, admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}
    form = get_form('Article')

