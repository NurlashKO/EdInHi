from django.conf.urls import url
from django import contrib

from . import views

urlpatterns = [
    url(r'^all/$', views.all_specializations_view, name='all_specializations'),
    url(r'^(?P<pk>[0-9]+)/$', views.specialization_view, name='specialization'),
]
