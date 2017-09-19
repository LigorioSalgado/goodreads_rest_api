from django.shortcuts import render, get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from .models import Book
from .serializers import BookSeriallizer, QuerysBookSerializer
from django.db.models import Q
# Create your views here.


class ListBook(APIView):

    def get(self, request):
        if request.query_params:
            queryparam = QuerysBookSerializer(data=request.query_params)
            if queryparam.is_valid():
                data = queryparam.validated_data
                books = Book.objects.filter(**data)
                serializer = BookSeriallizer(books, many=True)
                return Response(serializer.data, status=status.HTTP_200_OK)
            else:
                return Response(queryparam.errors,
                                status=status.HTTP_400_BAD_REQUEST)
        else:
            books = Book.objects.all()
            serializer = BookSeriallizer(books, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = BookSeriallizer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class DetailBook(APIView):

    def get(self, requets, pk):
        book = get_object_or_404(Book, pk=pk)
        serializer = BookSeriallizer(book)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, pk):
        book = get_object_or_404(Book, pk=pk)
        serializer = BookSeriallizer(book, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        book = get_object_or_404(Book, pk=pk)
        book.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
