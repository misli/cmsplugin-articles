# -*- coding: utf-8 -*-

from __future__ import absolute_import, division, generators, nested_scopes, print_function, unicode_literals, with_statement

from cms.menu_bases import CMSAttachMenu
from django.core.urlresolvers import reverse
from django.utils.translation import ugettext_lazy as _
from menus.base import NavigationNode

from .utils import get_model

class ArticlesMenu(CMSAttachMenu):

    name = _('Articles')

    def get_nodes(self, request):
        Article = get_model('Article')
        nodes = []
        try:
            years = months = days = slugs = []
            if request.user.is_staff:
                qs = Article.objects.all()
            else:
                qs = Article.objects.filter(public=True)
            for article in qs:
                pub_date = article.pub_date

                if not pub_date.year in years:
                    years.append(pub_date.year)
                    nodes.append(NavigationNode(pub_date.year,
                        reverse('Articles:year', kwargs={
                            'year': pub_date.year,
                        }), pub_date.year,
                    ))
                    months = []

                if not pub_date.month in months:
                    months.append(pub_date.month)
                    nodes.append(NavigationNode(_('{:%B}'.format(pub_date)),
                        reverse('Articles:month', kwargs={
                            'year': pub_date.year,
                            'month': '{:%m}'.format(pub_date),
                        }), '{:%m}'.format(pub_date), pub_date.year))
                    days = []

                if not pub_date.day in days:
                    days.append(pub_date.day)
                    nodes.append(NavigationNode('{:%d}'.format(pub_date),
                        reverse('Articles:day', kwargs={
                            'year':  pub_date.year,
                            'month': '{:%m}'.format(pub_date),
                            'day':   '{:%d}'.format(pub_date),
                        }), '{:%d}'.format(pub_date), '{:%m}'.format(pub_date)))
                    slugs = []

                if not article.slug in slugs:
                    slugs.append(article.slug)
                    nodes.append(NavigationNode(
                        article.title, article.get_absolute_url(), article.id, '{:%d}'.format(pub_date)))
        except:
            raise
        return nodes

