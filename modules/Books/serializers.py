from rest_framework import serializers
from .models import Book, GENEROS
from django.conf import settings
#from modules.Authors.serializers import AuthorSerializer


class BookSeriallizer(serializers.ModelSerializer):
    url_cover = serializers.SerializerMethodField()
    #author = AuthorSerializer(read_only=True)

    class Meta:
        model = Book
        fields = ('title', 'isbn', 'prologue', 'author',
                  'date_published', 'url_cover')

    def get_url_cover(self, obj):
        if "/media/" in obj.cover:
            return settings.CURRENT_HOST + obj.cover
        else:
            return obj.cover


class QuerysBookSerializer(serializers.Serializer):

    date_published = serializers.DateField(required=False)
    literary_genre = serializers.ChoiceField(choices=GENEROS, required=False)
    raiting = serializers.DecimalField(max_digits=3, decimal_places=2,
                                       required=False)
