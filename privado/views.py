from django.shortcuts import render, redirect
from privado.models import Time, Conflito
from privado.form import TimeForm, ConflitoForm

def time(request):
    time = Time.objects.all()
    parametros = {"time": time}  
    return render(request, "SAAB/time.html", parametros)

def createTime(request):
    formTime = TimeForm(request.POST or None)
    if formTime.is_valid():
        formTime.save()
        return redirect("/times")
    pacote = {"form": formTime}
    return render(request, "SAAB/formstime.html", pacote)

def updateTime(request, id):
    aval = Time.objects.get(pk=id)
    formTime = TimeForm(request.POST or None, instance=aval)
    if formTime.is_valid():
        formTime.save()
        return redirect("/times")
    pacote = {"form": formTime}
    return render(request, "SAAB/formstime.html", pacote)

def deleteTime(request, id):
    aval = Time.objects.get(pk=id)
    aval.delete()
    return redirect("/times")

    
def conflito(request):
    conflito = Conflito.objects.all()
    parametros = {"conflito": conflito}  
    return render(request, "SAAB/conflito.html", parametros)

def createConflito(request):
    formConflito = ConflitoForm(request.POST or None)
    if formConflito.is_valid():
        formConflito.save()
        return redirect("/conflitos")
    pacote = {"form": formConflito}
    return render(request, "SAAB/formsconflito.html", pacote)

def updateConflito(request, id):
    aval = Conflito.objects.get(pk=id)
    formConflito = ConflitoForm(request.POST or None, instance=aval)
    if formConflito.is_valid():
        formConflito.save()
        return redirect("/conflitos")
    pacote = {"form": formConflito}

def deleteConflito(request, id):
    aval = Conflito.objects.get(pk=id)
    aval.delete()
    return redirect("/conflitos")