# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from cms.models import Page, CMSPlugin, PlaceholderField
from django.core.exceptions import ValidationError
from django.core.urlresolvers import reverse
from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from django.utils.translation import ugettext_lazy as _
from polymorphic.polymorphic_model import PolymorphicModel

from .utils import get_html_field

# allow different implementation of HTMLField
HTMLField = get_html_field()



@python_2_unicode_compatible
class Article(PolymorphicModel):
    namespace   = models.CharField(_('Application instance'), max_length=200)
    title       = models.CharField(_('Title'), max_length=250)
    slug        = models.SlugField(_('Slug'), max_length=250, db_index=True, unique=False)
    pub_date    = models.DateField(_('Publication date'), editable=True)
    perex       = HTMLField(_('Perex'), blank=True, default='')
    text        = PlaceholderField('article_text')
    page_title  = models.CharField(_('Page title'), max_length=250, blank=True, null=True,
                    help_text=_('Overwrite the title (html title tag)'))
    menu_title  = models.CharField(_('Menu title'), max_length=250, blank=True, null=True,
                    help_text=_('Overwrite the title in the menu'))
    meta_desc   = models.TextField(_('Meta description'), blank=True, default='',
                    help_text=_('The text displayed in search engines.'))
    public      = models.BooleanField(default=False, verbose_name=_('Public'))

    class Meta:
        unique_together = [('pub_date', 'slug')]

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        errors = self._perform_unique_checks([(Article, ('pub_date', 'slug'))])
        if errors:
            raise ValidationError(errors)
        super(Article, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse(
            '{}:detail'.format(self.namespace),
            kwargs={
                'year': self.pub_date.year,
                'month':self.pub_date.month,
                'day':  self.pub_date.day,
                'slug': self.slug,
            },
        )

    def get_edit_url(self):
        return reverse('admin:{}_{}_change'.format(self._meta.app_label, self._meta.model_name), args=(self.id,))

    def get_page(self):
        return Page.objects.get(application_namespace=self.namespace, publisher_is_draft=False)

    def get_title(self):
        return self.title

    def get_page_title(self):
        return self.page_title or self.title

    def get_menu_title(self):
        return self.menu_title or self.title


