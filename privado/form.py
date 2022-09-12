from django.forms import ModelForm
from privado.models import Time, Conflito, Arbitro, Cidade

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
        fields = ["nome", "cidade", "formafisica"]

class CidadeForm(ModelForm):
    class Meta:
        model = Cidade
        fields = ["nome"]