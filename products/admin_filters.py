from django.contrib import admin
from django.utils.translation import ugettext_lazy as _

from . import utils


class DateAddedListFilter(admin.SimpleListFilter):
    # Human-readable title
    title = _('post date')

    # Parameter for the filter that will be used in the URL query.
    parameter_name = 'posted-ago'

    def lookups(self, request, model_admin):
        """
        Returns a list of tuples. The first element in each
        tuple is the coded value for the option that will
        appear in the URL query. The second element is the
        human-readable name for the option that will appear
        in the right sidebar.
        """
        return (
            ('last-day', _('The last day')),
            ('last-three-days', _('The last three days')),
            ('last-week', _('The last week')),
        )

    def queryset(self, request, queryset):
        """
        Returns the filtered queryset based on the value
        provided in the query string and retrievable via
        `self.value()`.
        """
        if self.value() == 'last-day':
            day_ranges = utils.get_last_n_days_frame(days=1)
            last_day_start, current_day_start = day_ranges
            return queryset.filter(date_added__gte=last_day_start,
                                   date_added__lt=current_day_start)
        if self.value() == 'last-three-days':
            three_day_ranges = utils.get_last_n_days_frame(days=3)
            last_three_days_start, current_day_start = three_day_ranges
            return queryset.filter(date_added__gte=last_three_days_start,
                                   date_added__lt=current_day_start)
        if self.value() == 'last-week':
            week_start, week_finish = utils.get_prev_week_frame(1)
            return queryset.filter(date_added__gte=week_start,
                                   date_added__lt=week_finish)


class DateUpdatedListFilter(admin.SimpleListFilter):
    # Human-readable title
    title = _('updated')

    # Parameter for the filter that will be used in the URL query.
    parameter_name = 'updated'

    def lookups(self, request, model_admin):
        """
        Returns a list of tuples. The first element in each
        tuple is the coded value for the option that will
        appear in the URL query. The second element is the
        human-readable name for the option that will appear
        in the right sidebar.
        """
        return (
            ('today', _('Today')),
        )

    def queryset(self, request, queryset):
        """
        Returns the filtered queryset based on the value
        provided in the query string and retrievable via
        `self.value()`.
        """
        if self.value() == 'today':
            current_day_start = utils.get_current_day_start()
            return queryset.filter(date_updated__gte=current_day_start)
