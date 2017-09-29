# Estas son cosas de Django
from django.shortcuts import render
from django.http import Http404
# Cosas de DRF
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
# Son mis cosas
from .serializers import AuthorSerializer
from .models import Author
# Create your views here.


class ListAuthor(APIView):
    """
        get:
        Return a list of authors
        post:
        Create an author in scratch
    """
    #

    def get(self, request):
        authors = Author.objects.all()  # querysets SELECT  * FROM Author
        serializer = AuthorSerializer(authors, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = AuthorSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class DetailAuthor(APIView):

    def _getAuthor(self, pk):
        try:
            return Author.objects.get(pk=pk)
            # SELECT * FROM AUTHOR WHERE id=PK AND name='George'
        except Author.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        author = self._getAuthor(pk)
        serializer = AuthorSerializer(author)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, pk):
        author = self._getAuthor(pk)
        serializer = AuthorSerializer(author, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        serializer = self._getAuthor(pk)
        serializer.delete()  # Hard Delete
        return Response(status=status.HTTP_204_NO_CONTENT)

    def patch(self, request, pk):
        author = self._getAuthor(pk)
        serializer = AuthorSerializer(author, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# @request(['GET'.'POST'])
# def index(request):
#     if request.method == 'GET':
#         pass
#     elif request.method == 'POST':
#         pass
#     else:
#         pass

#     pass
