from __future__ import absolute_import, division, generators, nested_scopes, print_function, unicode_literals, with_statement

import locale
import os
import string
from django.conf import settings
from django.utils.encoding import smart_text
from django.utils.translation import get_language, ugettext_lazy as _

try:
    from django.utils.module_loading import import_string
except ImportError:
    from django.utils.module_loading import import_by_path as import_string



def get_admin(name):
    return import_string(getattr(settings,
        'CMSPLUGIN_ARTICLES_{}_ADMIN'.format(name.upper()),
        'cmsplugin_articles.admins.{}Admin'.format(name),
    ))

def get_form(name):
    return import_string(getattr(settings,
        'CMSPLUGIN_ARTICLES_{}_FORM'.format(name.upper()),
        'cmsplugin_articles.forms.{}Form'.format(name),
    ))

def get_html_field():
    return import_string(getattr(settings,
        'CMSPLUGIN_ARTICLES_HTML_FIELD',
        'djangocms_text_ckeditor.fields.HTMLField',
    ))

def get_menu(name):
    return import_string(getattr(settings,
        'CMSPLUGIN_ARTICLES_{}_MENU'.format(name.upper()),
        'cmsplugin_articles.cms_menus.{}Menu'.format(name),
    ))

def get_model(name):
    return import_string(getattr(settings,
        'CMSPLUGIN_ARTICLES_{}_MODEL'.format(name.upper()),
        'cmsplugin_articles.models.{}'.format(name),
    ))

def get_plugin(name):
    return import_string(getattr(settings,
        'CMSPLUGIN_ARTICLES_{}_PLUGIN'.format(name.upper()),
        'cmsplugin_articles.plugins.{}Plugin'.format(name),
    ))

def get_toolbar(name):
    return import_string(getattr(settings,
        'CMSPLUGIN_ARTICLES_{}_TOOLBAR'.format(name.upper()),
        'cmsplugin_articles.cms_toolbars.{}Toolbar'.format(name),
    ))

def get_view(name):
    view = import_string(getattr(
        settings,
        'CMSPLUGIN_ARTICLES_{}_VIEW'.format(name.upper()),
        'cmsplugin_articles.views.{}'.format(name),
    ))
    return hasattr(view, 'as_view') and view.as_view() or view


# this is used to get all these names translated
WEEKDAYS = {
    0:_('Monday'), 1:_('Tuesday'), 2:_('Wednesday'), 3:_('Thursday'), 4:_('Friday'),
    5:_('Saturday'), 6:_('Sunday')
}
WEEKDAYS_ABBR = {
    0:_('Mon'), 1:_('Tue'), 2:_('Wed'), 3:_('Thu'), 4:_('Fri'),
    5:_('Sat'), 6:_('Sun')
}
MONTHS = {
    1:_('January'), 2:_('February'), 3:_('March'), 4:_('April'), 5:_('May'), 6:_('June'),
    7:_('July'), 8:_('August'), 9:_('September'), 10:_('October'), 11:_('November'),
    12:_('December')
}
MONTHS_ABBR = {
    1:_('jan'), 2:_('feb'), 3:_('mar'), 4:_('apr'), 5:_('may'), 6:_('jun'),
    7:_('jul'), 8:_('aug'), 9:_('sep'), 10:_('oct'), 11:_('nov'), 12:_('dec')
}


