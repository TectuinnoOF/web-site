from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.
class User(AbstractUser):
    ocupacion = models.CharField(max_length=60)
    area_interes = models.CharField(max_length=60)

    def __str__(self):
        return f"{self.username}  {self.last_name} ({self.email})"