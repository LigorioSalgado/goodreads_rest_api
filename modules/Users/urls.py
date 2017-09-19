from django.conf.urls import url
from django.contrib import admin
from .views import CreateUser


urlpatterns = [
    url(r'^$', CreateUser.as_view()),

]
