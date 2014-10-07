from __future__ import absolute_import, division, generators, nested_scopes, print_function, unicode_literals, with_statement

from cms.plugin_base import CMSPluginBase
from django.utils.translation import ugettext as _

from .utils import get_model



class ArticlePlugin(CMSPluginBase):
    model = get_model('ArticlePlugin')
    name = _('Article')
    text_enabled = True

    def render(self, context, instance, placeholder):
        context.update({
            'plugin': instance,
            'article': instance.article,
            'placeholder': placeholder,
        })
        return context



class LastArticlesPlugin(CMSPluginBase):
    model = get_model('LastArticlesPlugin')
    name = _('Last articles')
    text_enabled = True

    def render(self, context, instance, placeholder):
        context.update({
            'plugin': instance,
            'articles': instance.articles,
            'placeholder': placeholder,
        })
        return context

