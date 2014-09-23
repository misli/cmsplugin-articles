from __future__ import absolute_import, division, generators, nested_scopes, print_function, unicode_literals, with_statement

from django.views.generic import (
    ArchiveIndexView, YearArchiveView, MonthArchiveView,
    DayArchiveView, DateDetailView,
)

from .utils import get_model


class IndexView(ArchiveIndexView):
    model       = get_model('Article')
    date_field  = 'pub_date'

index = IndexView.as_view()



class YearView(YearArchiveView):
    model       = get_model('Article')
    date_field  = 'pub_date'

year = YearView.as_view()



class MonthView(MonthArchiveView):
    model       = get_model('Article')
    date_field  = 'pub_date'
    month_format= '%m'

month = MonthView.as_view()



class DayView(DayArchiveView):
    model       = get_model('Article')
    date_field  = 'pub_date'
    month_format= '%m'

day = DayView.as_view()



class DetailView(DateDetailView):
    model       = get_model('Article')
    date_field  = 'pub_date'
    month_format= '%m'

detail = DetailView.as_view()

