from django.conf.urls import url
from django import contrib

from . import views

urlpatterns = [
    url(r'^all_spec$', views.all_specializations, name='all_specializations'),
]
