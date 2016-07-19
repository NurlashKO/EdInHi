from django.conf.urls import url
from django import contrib

from . import views

urlpatterns = [
    url(r'^$', views.profile_view, name='profile'),
    url(r'^show/(?P<profile_id>[0-9]+)/$', views.profile_show, name='show_profile')
]
