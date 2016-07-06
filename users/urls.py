from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^all_users$', views.all_users, name='all_users'),
    url(r'^user/(?P<pk>[0-9]+)/', views.user_view, name='user'),
]
