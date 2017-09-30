from django.conf.urls import url
from django.contrib import admin
#from .views import ListBook, DetailBook
from .generic_views import ListBook, DetailBook, UpdateBookCover


urlpatterns = [
    url(r'^$', ListBook.as_view(), name='list_books'),
    url(r'^(?P<pk>[0-9]+)/$', DetailBook.as_view(), name='details_book'),
    url(r'^cover/(?P<pk>[0-9]+)/$', UpdateBookCover.as_view()),
]
