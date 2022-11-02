from django.shortcuts import render
from privado.models import Partida

def index(request):
    part = Partida.objects.all()
    patr_ordenados = part.order_by('-data')
    parametros = {"partidas": patr_ordenados}
    return render(request, "index.html", parametros)