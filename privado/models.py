from django.db import models
from django.contrib.auth.models import AbstractUser

class Usuario(AbstractUser):
    choices_tipo = (('G', 'Gerente'), ('A', 'Administrador'))
    tipo = models.CharField(max_length=1, choices=choices_tipo)

    def __str__(self):
        return (self.username)

class Cidade(models.Model):
    codigo = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=100)

    def __str__(self):
        return (self.nome)

class Time(models.Model):
    codigo = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=100)
    cidade = models.ForeignKey(Cidade, on_delete=models.CASCADE)

    def __str__(self):
        return (self.nome)

class Arbitro(models.Model):
    codigo = models.AutoField(primary_key=True)
    datanasc = models.DateField()
    cidade = models.ForeignKey(Cidade, on_delete=models.CASCADE)
    nome = models.CharField(max_length=100)
    formafisica = models.BooleanField()

    def __str__(self):
        return (self.nome)

class VidapubliArbitro(models.Model):
    codigo = models.AutoField(primary_key=True) 
    arbitro = models.ForeignKey(Arbitro, on_delete=models.CASCADE)
    descricao = models.TextField(max_length=260)
    data = models.DateField()
    peso = models.IntegerField()

class DeclaracaoArbitro(models.Model):
    codigo = models.AutoField(primary_key=True) 
    arbitro = models.ForeignKey(Arbitro, on_delete=models.CASCADE)
    descricao = models.TextField(max_length=260)
    data = models.DateField()
    peso = models.IntegerField()

class DenunciaArbitro(models.Model):
    codigo = models.AutoField(primary_key=True) 
    arbitro = models.ForeignKey(Arbitro, on_delete=models.CASCADE)
    descricao = models.TextField(max_length=260)
    data = models.DateField()
    peso = models.IntegerField()

class DocumentoArbitro(models.Model):
    codigo = models.AutoField(primary_key=True) 
    arbitro = models.ForeignKey(Arbitro, on_delete=models.CASCADE)
    descricao = models.TextField(max_length=260)
    data = models.DateField()
    peso = models.IntegerField()

class Partida(models.Model):
    codigo = models.AutoField(primary_key=True)
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    arbitro = models.ForeignKey(Arbitro, on_delete=models.CASCADE)
    visitante  = models.ForeignKey(Time, on_delete=models.CASCADE, related_name='visitante')
    local  = models.ForeignKey(Time, on_delete=models.CASCADE, related_name='local')
    data = models.DateField()

    def __str__(self):
        return str(self.codigo)

class Conflito(models.Model):
    codigo = models.AutoField(primary_key=True)
    partida = models.ForeignKey(Partida, on_delete=models.CASCADE)
    time = models.ForeignKey(Time, on_delete=models.CASCADE)
    descricao = models.TextField(max_length=260)
    errotecnico = models.BooleanField()