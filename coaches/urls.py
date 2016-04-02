from django.conf.urls import patterns, url
from coaches import views


urlpatterns = [
    url(r'(\d{1})/$', views.detail, name='detail'),
    ]
