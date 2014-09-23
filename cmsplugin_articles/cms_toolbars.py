from __future__ import unicode_literals

from cms.toolbar_base import CMSToolbar
from django.core.urlresolvers import reverse
from django.utils.translation import ugettext_lazy as _

from .utils import get_model

Article = get_model('Article')

class ArticlesToolbar(CMSToolbar):
    def populate(self):
        admin_menu = self.toolbar.get_or_create_menu('articles_menu', _('Articles'))
        admin_menu.add_modal_item(_('List articles'), url=reverse('admin:{}_{}_changelist'.format(Article._meta.app_label, Article._meta.model_name)))
        admin_menu.add_modal_item(_('Add article'), url=reverse('admin:{}_{}_add'.format(Article._meta.app_label, Article._meta.model_name)))
