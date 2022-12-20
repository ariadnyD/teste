from django.shortcuts import render
from privado.models import *

def index(request):
    part = Partida.objects.all()
    patr_ordenados = part.order_by('-data')
    parametros = {"partidas": patr_ordenados}
    return render(request, "index.html", parametros)

def sobre(request):
    part = Partida.objects.all()
    patr_ordenados = part.order_by('-data')
    parametros = {"partidas": patr_ordenados}
    return render(request, "about.html", parametros)

def search(request):
    results =[]
    if request.method =="GET":
        query = request.GET.get('site_search')
        print(query)
        results = Partida.objects.filter(nome__icontains=query)
        print(results)

    return render(request, 'indexbusca.html', {'query':query, 'results': results})