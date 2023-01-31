from django import forms as django_forms
from django.contrib.auth import forms
from django.forms import ModelForm
from privado.models import Time, Conflito, Arbitro, Cidade, DeclaracaoArbitro, VidapubliArbitro,  DenunciaArbitro, DocumentoArbitro, Partida, Usuario

class UserChangeForm(forms.UserChangeForm):
    class Meta(forms.UserChangeForm.Meta):
        model = Usuario

class UserCreationForm(forms.UserCreationForm):
    first_name = django_forms.CharField(max_length=150, label="Nome", required=False)
    username = django_forms.EmailField(max_length=150, label="E-mail", required=True)
    class Meta:
        model = Usuario
        fields = ["first_name", "username", "password1", "password2"]

    def __init__(self, *args, **kwargs):
        super(UserCreationForm, self).__init__(*args, **kwargs)

        for fieldname in ['username', 'password1', 'password2']:
            self.fields[fieldname].help_text = None

class TimeForm(ModelForm):
    class Meta:
        model = Time
        fields = ["nome", "cidade"]
        labels = {
            "nome": "Nome do time:",
            "cidade": "Cidade:",
        }

class ConflitoForm(django_forms.Form):
    time = django_forms.ModelChoiceField(queryset=Time.objects.all(), label="Selecione o time envolvido", required=False)
    descricao = django_forms.CharField(label="Descreva o conflito e a relação do time selecionado com ele.", required=False)
    errotecnico = django_forms.BooleanField(label="Foi um erro técnico do arbitro?", required=False)

class ConflitoModelForm(ModelForm):
    class Meta:
        model = Conflito
        fields = ["partida", "time", "descricao", "errotecnico"]
        labels = {
            "partida": "Código da partida:",
            "time": "Time:",
            "descricao": "Descrição do conflito:",
            "errotecnico": "Marque apenas se o conflito se caracteriza como erro técnico",
        }

class ArbitroForm(ModelForm):
    class Meta:
        model = Arbitro
        fields = ["nome", "datanasc", "cidade", "formafisica"]
        labels = {
            "nome": "Nome do árbitro:",
            "datanasc": "Data de nascimento:",
            "cidade": "Cidade natal:",
            "formafisica": "Marque apenas se o ábritro se apresenta em boa forma física",
        }

class CidadeForm(ModelForm):
    class Meta:
        model = Cidade
        fields = ["nome"]
        labels = {
            "nome": "Nome da cidade:",
        }

class PartidaForm(django_forms.Form):
    nome = django_forms.CharField(label="Nome: (ex: Local x Visitante)", required=False)
    local = django_forms.ModelChoiceField(queryset=Time.objects.all(), label="Selecione o time local", required=False)
    visitante = django_forms.ModelChoiceField(queryset=Time.objects.all(), label="Selecione o time visitante", required=False)
    data = django_forms.DateField(label="Data da partida", required=False)

class PartidaModelForm(ModelForm):
    class Meta:
        model = Partida
        fields = ["nome", "local", "visitante", "data"]
        labels = {
            "nome": "Nome da partida:",
            "local": "Time da casa:",
            "visitante": "Time visitante:",
            "data": "Data da partida:",
        }

class PolemicaModelForm(ModelForm):
    class Meta:
        model = DeclaracaoArbitro
        fields = ["descricao","data","peso"]
        labels = {
            "descricao": "Descrição:",
            "data": "Data do ocorrido:",
            "peso": "Peso:",
        }

class PolemicaForm(django_forms.Form):
    descricao = django_forms.CharField(widget=django_forms.Textarea, max_length=400, label="Descrição:")
    data = django_forms.DateField(label="Data do ocorrido:", required=False)
    peso = django_forms.IntegerField(label="Peso:")

class PolemicaVPModelForm(ModelForm):
    class Meta:
        model = VidapubliArbitro
        fields = ["descricao","data","peso" ]
        labels = {
            "descricao": "Descrição:",
            "data": "Data do ocorrido:",
            "peso": "Peso:",
        }

class PolemicaVPForm(django_forms.Form):
    descricao = django_forms.CharField(widget=django_forms.Textarea, max_length=400, label="Descrição:")
    data = django_forms.DateField(label="Data do ocorrido:", required=False)
    peso = django_forms.IntegerField(label="Peso:")

class DenunciasModelForm(ModelForm):
    class Meta:
        model = DenunciaArbitro
        fields = ["descricao","data","peso" ]
        labels = {
            "descricao": "Descrição:",
            "data": "Data do ocorrido:",
            "peso": "Peso:",
        }

class DenunciasForm(django_forms.Form):
    descricao = django_forms.CharField(widget=django_forms.Textarea, max_length=400, label="Descrição:")
    data = django_forms.DateField(label="Data do ocorrido:", required=False)
    peso = django_forms.IntegerField(label="Peso:")

class PapeladaModelForm(ModelForm):
    class Meta:
        model = DocumentoArbitro
        fields = ["descricao","data","peso" ]
        labels = {
            "descricao": "Descrição:",
            "data": "Data do ocorrido:",
            "peso": "Peso:",
        }

class PapeladaForm(django_forms.Form):
    descricao = django_forms.CharField(widget=django_forms.Textarea, max_length=400, label="Descrição:")
    data = django_forms.DateField(label="Data do ocorrido:", required=False)
    peso = django_forms.IntegerField(label="Peso:")

