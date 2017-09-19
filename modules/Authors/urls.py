from django.conf.urls import url
from django.contrib import admin
from .views import ListAuthor, DetailAuthor

urlpatterns = [
    url(r'^$', ListAuthor.as_view()),
    url(r'^(?P<pk>[0-9]+)/$', DetailAuthor.as_view()),
]
