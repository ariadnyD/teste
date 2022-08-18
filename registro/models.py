from django.db import models

# Create your models here.

class registro(models.Model):
    nome = models.CharField(max_length=100)
    telefone = models.IntegerField()
    nascimento = models.DateField()
    email = models.EmailField()
    senha = models.CharField(max_length=50)
    confirme_senha = models.CharField(max_length=50)

    def __str__ (self):
        return self.nome
