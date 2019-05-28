from rest_framework import generics

from . import models
from . import serializers


class ProductList(generics.ListCreateAPIView):
    """
    View for listing or creating products.
    """
    queryset = models.Product.objects.all()
    serializer_class = serializers.ProductSerializer
