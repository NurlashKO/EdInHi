from django.conf.urls import url
from django import contrib
from . import views

urlpatterns = [
    url(r'^authentification/', views.auth_view, name='authentification')
]
