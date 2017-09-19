from rest_framework import generics, filters
from .models import Book
from .serializers import BookSeriallizer
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.permissions import IsAuthenticated


class ListBook(generics.ListCreateAPIView):
    # Get y POST
    serializer_class = BookSeriallizer
    queryset = Book.objects.all()
    filter_backends = (filters.SearchFilter, DjangoFilterBackend)
    filter_fields = ('raiting', 'date_published', 'price', 'literary_genre')
    search_fields = ('title', 'prologue', 'literary_genre')
    permission_classes = (IsAuthenticated,)


class DetailBook(generics.RetrieveUpdateDestroyAPIView):
    # Get,Put,Delete y Patch
    serializer_class = BookSeriallizer
    queryset = Book.objects.all()
