from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.ProductList.as_view(), name='list'),
    url(r'^(?P<pk>\d+)$', views.ProductDetailView.as_view(), name='detail'),
]
