from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.company_view, name='company'),
    url(r'^add_vacancy', views.company_add_vacancy, name='company_add_vacancy'),
    url(r'^delete_vacancy/(?P<pk>[0-9]+)/', views.company_delete_vacancy, name='company_delete_vacancy'),
]
