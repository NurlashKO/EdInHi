from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.feedback_view, name='feedback'),
    url(r'^send_feedback', views.send_feedback_view, name='send_feedback'),
]
