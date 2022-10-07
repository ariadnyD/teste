from django.shortcuts import render, redirect
from privado.models import Time, Conflito, Arbitro, Cidade, VidapubliArbitro, DeclaracaoArbitro, DenunciaArbitro, DocumentoArbitro, Partida
from privado.form import *
from django.db.models.aggregates import Count

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

def detalhamentoArbitro(request, id):
    arbi = Arbitro.objects.get(pk=id)
    ContDe= DeclaracaoArbitro.objects.filter(arbitro = id). aggregate(decla_count=Count ('*'))
    ContDenun= DenunciaArbitro.objects.filter(arbitro = id). aggregate(denun_count=Count ('*'))
    ContVp= VidapubliArbitro.objects.filter(arbitro = id). aggregate(vp_count=Count ('*'))
    ContDoc= DocumentoArbitro.objects.filter(arbitro = id). aggregate(doc_count=Count ('*'))
    context = {
        'arbitro': arbi,
        'ContDe': ContDe,
        'ContDenun': ContDenun,
        'ContVp': ContVp,
        'ContDoc': ContDoc
    }

    return render(request, "SAAB/detalhamentoArbitro.html", context)

def InfoAdicionais (request, id):
    arbi = Arbitro.objects.get(pk=id)
    Decla = DeclaracaoArbitro.objects.filter(arbitro=id)
    Denun = DenunciaArbitro.objects.filter(arbitro=id)
    VidaPub = VidapubliArbitro.objects.filter(arbitro=id)
    Doc = DocumentoArbitro.objects.filter(arbitro=id)
    context = {
        'arbitro': arbi,
        'Decla': Decla,
        'Denun': Denun,
        'VidaPub': VidaPub,
        'Doc': Doc
    }
    return render(request, "SAAB/InfoAdicionais.html", context)

def formPolemica(request, id):
    formPolemica = PolemicaForm(request.POST or None)
    if formPolemica.is_valid() :
        formPolemica.save()
        return redirect("/InfoAdicionais/"+str(id))

    pacote = {"formPolemica": formPolemica}
    return render(request, "SAAB/formPolemica.html", pacote)

def updatePolemica(request, ida, id):
    pole = DeclaracaoArbitro.objects.get(pk=id)
    formPolemica = PolemicaForm(request.POST or None, instance=pole)
    if formPolemica.is_valid():
        formPolemica.save()
        return redirect("/InfoAdicionais/"+str(ida))

    pacote = {"formPolemica": formPolemica}
    return render(request, "SAAB/formPolemica.html", pacote)

def deletePolemica(request, ida, id):
    pole = DeclaracaoArbitro.objects.get(pk=id)
    pole.delete()
    return redirect("/InfoAdicionais/"+str(ida))

def formPolemicaVP(request, id):
    formPolemicaVP = PolemicaVPForm(request.POST or None)
    if formPolemicaVP.is_valid() :
        formPolemicaVP.save()
        return redirect("/InfoAdicionais/"+str(id))

    pacote = {"formPolemicaVP": formPolemicaVP}
    return render(request, "SAAB/formPolemicaVP.html", pacote)

def updatePolemicaVP(request, ida, id):
    polevp = VidapubliArbitro.objects.get(pk=id)
    formPolemicaVP = PolemicaVPForm(request.POST or None, instance=polevp)
    if formPolemicaVP.is_valid() :
        formPolemicaVP.save()
        return redirect("/InfoAdicionais/"+str(ida))

    pacote = {"formPolemicaVP": formPolemicaVP}
    return render(request, "SAAB/formPolemicaVP.html", pacote)

def deletePolemicaVP(request, ida, id):
    polevp = VidapubliArbitro.objects.get(pk=id)
    polevp.delete()
    return redirect("/InfoAdicionais/"+str(ida))
    
def formDenuncias(request, id):
    formDenuncias = DenunciasForm(request.POST or None)
    if formDenuncias.is_valid() :
        formDenuncias.save()
        return redirect("/InfoAdicionais/"+str(id))

    pacote = {"formDenuncias": formDenuncias}
    return render(request, "SAAB/formDenuncias.html", pacote)

def updateDenuncias(request, ida, id):
    denuncia = DenunciaArbitro.objects.get(pk=id)
    formDenuncias = DenunciasForm(request.POST or None, instance=denuncia)
    if formDenuncias.is_valid() :
        formDenuncias.save()
        return redirect("/InfoAdicionais/"+str(ida))

    pacote = {"formDenuncias": formDenuncias}
    return render(request, "SAAB/formDenuncias.html", pacote)

def deleteDenuncias(request, ida, id):
    denuncia = DenunciaArbitro.objects.get(pk=id)
    denuncia.delete()
    return redirect("/InfoAdicionais/"+str(ida))

def formPapelada(request, id):
    formPapelada = PapeladaForm(request.POST or None)
    if formPapelada.is_valid() :
        formPapelada.save()
        return redirect("/InfoAdicionais/"+str(id))

    pacote = {"formPapelada": formPapelada}
    return render(request, "SAAB/formPapelada.html", pacote)

def updatePapelada(request, ida, id):
    papelada = DocumentoArbitro.objects.get(pk=id)
    formPapelada = PapeladaForm(request.POST or None, instance=papelada)
    if formPapelada.is_valid() :
        formPapelada.save()
        return redirect("/InfoAdicionais/"+str(ida))

    pacote = {"formPapelada": formPapelada}
    return render(request, "SAAB/formPapelada.html", pacote)

def deletePapelada(request, ida, id):
    papelada = DocumentoArbitro.objects.get(pk=id)
    papelada.delete()
    return redirect("/InfoAdicionais/"+str(ida))

def sorteio(request):
    formPartida = PartidaForm(request.POST or None)
    arbt = Arbitro.objects.all()
    if formPartida.is_valid() :
        formPartida.save()
        return redirect("/")
    pacote = {"formPartida": formPartida, "arbitros": arbt}
    return render(request, "SAAB/sorteio.html", pacote)

def inicioAdmin(request):
    part = Partida.objects.all()
    parametros = {"partidas": part}  
    return render(request, "SAAB/partidas.html", parametros)

def updatePartida(request, id):
    partida = Partida.objects.get(pk=id)
    formPartida = PartidaForm(request.POST or None, instance=partida)

    if formPartida.is_valid():
        formPartida.save()
        return redirect('url_partida')

    pacote = {"formPartida": formPartida}
    return render(request, "SAAB/formPartida.html", pacote)

def deletePartida(request, id):
    partida = Partida.objects.get(pk=id)
    partida.delete()
    return redirect("/partidas")

def detalhamentoPartida(request, id):
    conflitos = Conflito.objects.all()
    partida = Partida.objects.filter(pk=id)
    time = Time.objects.filter(pk=id)
    detalhes = {"detalhes":partida, "conflitos":conflitos, "time":time}
    return render(request, "SAAB/detalhamentoPartida.html", detalhes)



   
