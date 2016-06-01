from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^(?P<skill_id>[0-9]+)/', views.skill, name='skill'),
]
