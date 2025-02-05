from django.db import models
# Create your models here.
from django.db import models
from django.contrib.auth.models import User

class PerfilUsuario(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    telefono = models.CharField(max_length=15, blank=True)
    direccion = models.CharField(max_length=255, blank=True)
    char_length = models.PositiveIntegerField(default=8)
    min_nums = models.PositiveIntegerField(default=1)
    min_minus = models.PositiveIntegerField(default=1)
    min_mayus = models.PositiveIntegerField(default=1)
    min_simbolos = models.PositiveIntegerField(default=1)

    def __str__(self):
        return self.user.username

