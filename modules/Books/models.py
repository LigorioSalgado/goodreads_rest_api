from django.db import models
from django.contrib.postgres.fields import ArrayField
from modules.Authors.models import Author
#from django.contrib.auth.models import User
from django.conf import settings
# Create your models here.
GENEROS = (
    ("CS", "Ciencia Ficción"),
    ("FS", "Fantasia"),
    ("TR", "Terror"),
    ("IT", "Tecnología"),
    ("DR", "Drama")
)


class Book(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100, help_text="El titulo del libro")
    author = models.ForeignKey(
        Author, on_delete=models.CASCADE, related_name='books')
    isbn = models.CharField(max_length=100)
    date_published = models.DateField(
        help_text="Este es la fecha de publicaciòn")
    cover = models.URLField()
    prologue = models.TextField()
    raiting = models.DecimalField(decimal_places=1, max_digits=3)
    literary_genre = models.CharField(choices=GENEROS, max_length=50)
    tags = ArrayField(
        models.CharField(max_length=50), blank=True, null=True
    )
    price = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return "Book:{0}".format(self.title)


class Comments(models.Model):
    id = models.AutoField(primary_key=True)
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="comentarista")
    book = models.ForeignKey(
        Book, on_delete=models.CASCADE, related_name="libro")
    commet = models.TextField()

    def __str__(self):
        return "Comment of user :{0} and book: {1} ".format(
            self.author.first_name,
            self.book.title)

    def __unicode__(self):
        return
