from wsgiref.handlers import format_date_time
from django.db import models

class Usuario(models.Model):
    codigo = models.AutoField(primary_key=True)
    username = models.CharField(max_length=16)
    email = models.CharField(max_length=100)
    senha = models.CharField(max_length=16)

class Cidade(models.Model):
    codigo = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=100)

class Time(models.Model):
    codigo = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=100)
    cidade = models.ForeignKey(Cidade, on_delete=models.CASCADE)

class Arbitro(models.Model):
    codigo = models.AutoField(primary_key=True)
    cidade = models.ForeignKey(Cidade, on_delete=models.CASCADE)
    nome = models.CharField(max_length=100)
    formafisica = models.BooleanField()

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
    visitante = models.ForeignKey(Time, on_delete=models.CASCADE)
    data = models.DateField()

class Conflito(models.Model):
    codigo = models.AutoField(primary_key=True)
    partida = models.ForeignKey(Partida, on_delete=models.CASCADE)
    time = models.ForeignKey(Time, on_delete=models.CASCADE)
    descricao = models.TextField(max_length=260)
    errotecnico = models.BooleanField()

