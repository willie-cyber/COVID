from django.db import models
from django.contrib.auth.models import User


GENERO = (
    (1, 'MASCULINO'),
    (2, 'FEMENINO'),
)

ESTATUS = (
    (1, 'ENFERMOS'),
    (2, 'RECUPERADOS'),
    (3, 'FALLECIDOS')
)

class Covid(models.Model):
    date = models.DateField("Fecha")
    name = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    age = models.IntegerField(default=0)
    country = models.CharField(max_length=30)
    gender = models.PositiveSmallIntegerField(choices=GENERO)
    status = models.PositiveSmallIntegerField(choices=ESTATUS)

    def __str__(self):
        return self.country


