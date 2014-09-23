from __future__ import unicode_literals

from django.contrib import admin
from .utils import get_model, get_admin

admin.site.register(get_model('Article'), get_admin('Article'))

