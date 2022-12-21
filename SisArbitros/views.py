from django.shortcuts import render
from privado.models import Partida, Conflito

def index(request):
    part = Partida.objects.all()
    conf = Conflito.objects.all().order_by('-codigo')[:10]
    conf1 = conf[:1]
    conf = conf[1:10]
    patr_ordenados = part.order_by('-data')[:30]
    parametros = {"partidas": patr_ordenados, "conflitos": conf, "conflito1": conf1}
    return render(request, "index.html", parametros)

def sobre(request):
    part = Partida.objects.all()
    patr_ordenados = part.order_by('-data')
    parametros = {"partidas": patr_ordenados}
    return render(request, "about.html", parametros)

def search(request):
    results =[]
    if request.method =="GET":
        patr = Partida.objects.all()
        query = request.GET.get('site_search')
        results = patr.filter(nome__icontains=query)

    return render(request, 'indexbusca.html', {'query':query, 'results': results})