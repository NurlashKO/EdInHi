from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.company_view, name='company'),
    url(r'^add_task', views.company_add_task, name='company_add_task')
]
