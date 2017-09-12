from django.db import models

# Create your models here.
NACIONALIDADES = (
    ("USA", "Estadounidense"),
    ("MX", "Mexicana"),
    ("ES", "Español"),
    ("FR", "Frances"),
    ("IN", "Ingles")
)


class Author(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    nacionalidad = models.CharField(choices=NACIONALIDADES, max_length=50)
    biography = models.TextField()
    gender = models.CharField(choices=(('M', 'Masculino'), ('F', 'Femenino')),
                              max_length=50)
    age = models.IntegerField()
    is_alive = models.BooleanField(default=True)

    def __str__(self):
        return "Author:{0} {1}".format(self.name, self.last_name)
