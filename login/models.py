from django.db import models

# Create your models here.

class login(models.Model):
    login = models.CharField(max_length=50)
    senha = models.CharField(max_length=50)

    