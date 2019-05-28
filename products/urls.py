from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.ProductList.as_view(), name='list')
]
