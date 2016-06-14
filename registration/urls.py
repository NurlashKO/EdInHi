from django.conf.urls import url
from django import contrib

from . import views

urlpatterns = [
    url(r'^sign_in', views.auth_view, name='auth'),
    url(r'^sign_up', views.reg_view, name='reg'),
    url(r'^sign_out', views.logout_view, name='sign_out'),
    url(r'^company_sign_up', views.company_reg_view, name='company_reg'),
]
