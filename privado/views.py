from django.shortcuts import render, redirect
from privado.models import Time
from privado.form import TimeForm

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
