from rest_framework import serializers
from .models import Author
from modules.Books.serializers import BookSeriallizer


def name_only_edwin(source):
    if source == "Edwin" or "edwin":
        pass
    else:
        raise serializers.ValidationError("No te llamas edwin")


class ExampleSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=50, validators=[name_only_edwin])
    last_name = serializers.CharField(max_length=50)
    birth_date = serializers.DateField()
    age = serializers.IntegerField()
    price = serializers.DecimalField(max_digits=10, decimal_places=2)


class AuthorSerializer(serializers.ModelSerializer):
    #books = BookSeriallizer(read_only=True, many=True)

    class Meta:
        model = Author
        fields = '__all__'
       # exclude = ('is_alive',)

    def delete(self, entry):
        pass
