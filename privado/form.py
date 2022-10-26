from threading import local
from django import forms as django_forms
from django.contrib.auth import forms
from django.forms import ModelForm
from privado.models import Time, Conflito, Arbitro, Cidade, DeclaracaoArbitro, VidapubliArbitro,  DenunciaArbitro, DocumentoArbitro, Partida

class TimeForm(ModelForm):
    class Meta:
        model = Time
        fields = ["codigo", "nome", "cidade"]

class ConflitoForm(ModelForm):
    class Meta:
        model = Conflito
        fields = ["codigo", "partida", "time", "descricao", "errotecnico"]

class ArbitroForm(ModelForm):
    class Meta:
        model = Arbitro
        fields = ["nome", "datanasc", "cidade", "formafisica"]

class CidadeForm(ModelForm):
    class Meta:
        model = Cidade
        fields = ["nome"]

class PartidaForm(django_forms.Form):
    visitante = django_forms.ModelChoiceField(queryset=Time.objects.all(), label="Selecione o time visitante")
    local = django_forms.ModelChoiceField(queryset=Time.objects.all(), label="Selecione o time local")
    data = django_forms.DateField(label="Data da partida")

class PolemicaForm(ModelForm):
    class Meta:
        model = DeclaracaoArbitro
        fields = ["codigo" , "arbitro","descricao","data","peso" ]

class PolemicaVPForm(ModelForm):
    class Meta:
        model = VidapubliArbitro
        fields = ["codigo" , "arbitro","descricao","data","peso" ]

class DenunciasForm(ModelForm):
    class Meta:
        model = DenunciaArbitro
        fields = ["codigo" , "arbitro","descricao","data","peso" ]

class PapeladaForm(ModelForm):
    class Meta:
        model = DocumentoArbitro
        fields = ["codigo" , "arbitro","descricao","data","peso" ]

