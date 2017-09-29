from rest_framework import generics, filters, status
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from .models import Book
from rest_framework.response import Response
from .serializers import BookSeriallizer
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.permissions import IsAuthenticated
from rest_framework.parsers import FormParser, MultiPartParser
from django.conf import settings


class ListBook(generics.ListCreateAPIView):
    # Get y POST
    serializer_class = BookSeriallizer
    queryset = Book.objects.all()
    filter_backends = (filters.SearchFilter, DjangoFilterBackend)
    filter_fields = ('raiting', 'date_published', 'price', 'literary_genre')
    search_fields = ('title', 'prologue', 'literary_genre')
    #permission_classes = (IsAuthenticated,)


class DetailBook(generics.RetrieveUpdateDestroyAPIView):

    # Get,Put,Delete y Patch
    serializer_class = BookSeriallizer
    queryset = Book.objects.all()


class UpdateBookCover(APIView):
    parser_classes = (FormParser, MultiPartParser)

    def handle_uploaded_file(self, f):
        path = "%s/%s" % (settings.MEDIA_ROOT, str(f))

        with open(path, 'wb+') as destination:
            for chunk in f.chunks():
                destination.write(chunk)
        return "%s/%s" % (settings.MEDIA_URL, str(f))

    def patch(self, request, pk):
        book = get_object_or_404(Book, id=pk)
        try:
            path = self.handle_uploaded_file(request.FILES['file'])
            book.cover = path
            book.save(update_fields=['cover'])
            # Book.objects.filter(id=pk).update(cover=path)
        except:
            return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        return Response(status=status.HTTP_200_OK)
