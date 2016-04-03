from django.conf.urls import patterns, url
from .views import *


urlpatterns = [
    url(r'^(?P<pk>\d+)/$', CoachDetailView.as_view(), name="detail"),
    ]
