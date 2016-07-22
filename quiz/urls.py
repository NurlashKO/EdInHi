from django.conf.urls import url
from django import contrib

from . import views

urlpatterns = [
    url(r'^(?P<quiz_id>[0-9]+)/', views.quiz_view, name='quiz'),
    url(r'^quiz_submit/(?P<skill_id>[0-9]+)/', views.quiz_submit_view, name='quiz_submit')
]
