from django.conf.urls import url
from django import contrib
from . import views

urlpatterns = [
    url(r'^all/$', views.all_specializations_view, name='all_specializations'),
    url(r'^(?P<pk>[0-9]+)/$', views.specialization_view, name='specialization'),
    url(r'^delete_from_wishlist/(?P<pk>[0-9]+)/', views.delete_from_wishlist, name='delete_from_wishlist'),
]
