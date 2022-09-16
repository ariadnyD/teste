from django.shortcuts import render
from privado.models import Partida

def index(request):
    part = Partida.objects.all()
    parametros = {"partidas": part}  
    return render(request, "index.html", parametros)