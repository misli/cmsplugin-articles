from __future__ import absolute_import, division, generators, nested_scopes, print_function, unicode_literals, with_statement

from django.contrib import admin
from .utils import get_model, get_admin

admin.site.register(get_model('Article'), get_admin('Article'))

