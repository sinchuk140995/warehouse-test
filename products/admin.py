from django.contrib import admin

from . import admin_filters
from . import models


@admin.register(models.Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'date_updated', 'date_added')
    list_display_links = ('name', 'date_updated', 'date_added')
    list_filter = (admin_filters.DateAddedListFilter,
                   admin_filters.DateUpdatedListFilter)
