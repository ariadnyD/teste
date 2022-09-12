from django.shortcuts import render, redirect
from privado.models import Time, Conflito, Arbitro, Cidade
from privado.form import TimeForm, ConflitoForm, ArbitroForm, CidadeForm

# essa função é só por enquanto
def index(request):
    return render(request, "SAAB/layout.html")

def login(request):
    return render(request, "SAAB/login.html")

def times(request):
    time = Time.objects.all()
    parametros = {"time": time}  
    return render(request, "SAAB/times.html", parametros)

def formTime(request):
    formTime = TimeForm(request.POST or None)
    if formTime.is_valid():
        formTime.save()
        return redirect("/times")
    pacote = {"form": formTime}
    return render(request, "SAAB/formTime.html", pacote)

def updateTime(request, id):
    aval = Time.objects.get(pk=id)
    formTime = TimeForm(request.POST or None, instance=aval)
    if formTime.is_valid():
        formTime.save()
        return redirect("/times")
    pacote = {"form": formTime}
    return render(request, "SAAB/formTime.html", pacote)

def deleteTime(request, id):
    aval = Time.objects.get(pk=id)
    aval.delete()
    return redirect("/times")

def conflitos(request):
    conflito = Conflito.objects.all()
    parametros = {"conflito": conflito}
    return render(request, "SAAB/conflitos.html", parametros)

def formConflito(request):
    formConflito = ConflitoForm(request.POST or None)
    if formConflito.is_valid():
        formConflito.save()
        return redirect("/conflitos")
    pacote = {"form": formConflito}
    return render(request, "SAAB/formconflito.html", pacote)

def updateConflito(request, id):
    aval = Conflito.objects.get(pk=id)
    formConflito = ConflitoForm(request.POST or None, instance=aval)
    if formConflito.is_valid():
        formConflito.save()
        return redirect("/conflitos")
    pacote = {"form": formConflito}
    return render(request, "SAAB/formConflito.html", pacote)

def deleteConflito(request, id):
    aval = Conflito.objects.get(pk=id)
    aval.delete()
    return redirect("/conflitos")

def arbitros(request):
    arbt = Arbitro.objects.all()
    pacote = {"arbitros": arbt, "editArbitro": 123}
    return render(request, "SAAB/arbitros.html", pacote)

def cidades(request):
    cidd = Cidade.objects.all()
    pacote = {"cidades": cidd, "editCidade": 123}
    return render(request, "SAAB/cidades.html", pacote)

def formArbitro(request):
    formArbitro = ArbitroForm(request.POST or None)
    if formArbitro.is_valid() :
        formArbitro.save()
        return redirect("/arbitros")

    pacote = {"formArbitro": formArbitro}
    return render(request, "SAAB/formArbitro.html", pacote)

def updateArbitro(request, id):
    arbi = Arbitro.objects.get(pk=id)
    formArbitro = ArbitroForm(request.POST or None, instance=arbi)
    if formArbitro.is_valid() :
        formArbitro.save()
        return redirect("/arbitros")

    pacote = {"formArbitro": formArbitro}
    return render(request, "SAAB/formArbitro.html", pacote)

def deleteArbitro(request, id):
    arbi = Arbitro.objects.get(pk=id)
    arbi.delete()
    return redirect("/arbitros")

def formCidade(request):
    formCidade = CidadeForm(request.POST or None)
    if formCidade.is_valid() :
        formCidade.save()
        return redirect("/cidades")

    pacote = {"formCidade": formCidade}
    return render(request, "SAAB/formCidade.html", pacote)

def updateCidade(request, id):
    cida = Cidade.objects.get(pk=id)
    formCidade = CidadeForm(request.POST or None, instance=cida)
    if formCidade.is_valid() :
        formCidade.save()
        return redirect("/cidades")

    pacote = {"formCidade": formCidade}
    return render(request, "SAAB/formCidade.html", pacote)

def deleteCidade(request, id):
    cida = Cidade.objects.get(pk=id)
    cida.delete()
    return redirect("/cidades")