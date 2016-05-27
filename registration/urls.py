from django.conf.urls import url
from django import contrib
from . import views

urlpatterns = [
    url(r'^registration/', views.login_view, name='registration'),
]
