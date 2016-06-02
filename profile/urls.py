from django.conf.urls import url
from django import contrib

from . import views

urlpatterns = [
    url(r'^$', views.profile_view, name='profile'),
]