from django.conf.urls import patterns, include, url
from students.views import *

urlpatterns = [
    url(r'^add/', StudentCreateView.as_view(), name="add"),
    url(r'^edit/(?P<pk>\d+)/$', StudentUpdateView.as_view(), name="edit"),
    url(r'^remove/(?P<pk>\d+)/$', StudentDeleteView.as_view(), name="remove"),
    url(r'^(?P<pk>\d+)/$', StudentDetailView.as_view(), name='detail'),
    url(r'^$', StudentListView.as_view(), name='list_view'),
]
