from django.db import models
from django.utils.translation import ugettext_lazy as _


class Product(models.Model):
    name = models.CharField(_('name'), max_length=50, unique=True)
    description = models.TextField(_('description'))
    date_added = models.DateTimeField(_('post date'), auto_now_add=True)
    date_updated = models.DateTimeField(_('updated'), auto_now=True)

    class Meta:
        ordering = ('-date_added',)

    def __str__(self):
        return self.name
