from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^allcompanies/', views.all_companies, name='all_companies'),
    url(r'^company/(?P<pk>[0-9]+)/', views.detail_company, name='detail_company'),
]