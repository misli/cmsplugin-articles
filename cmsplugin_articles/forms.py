# -*- coding: utf-8 -*-

from __future__ import absolute_import, division, generators, nested_scopes, print_function, unicode_literals, with_statement

from cms.models import Page
from django import forms

from .utils import get_model


class ArticleForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(ArticleForm, self).__init__(*args, **kwargs)
        choices = (
            (page.application_namespace, page.get_title())
            for page in Page.objects.filter(application_urls='ArticlesApp', publisher_is_draft=True)
        )
        if hasattr(self.fields['namespace'].widget, 'choices'):
            self.fields['namespace'].widget.choices = choices
        else:
            self.fields['namespace'].widget = forms.Select(choices = choices)

    class Meta:
        model   = get_model('Article')


