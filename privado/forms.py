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
    visitante = django_forms.ModelChoiceField(queryset=Time.objects.all(), label="Selecione o time visitante", required=False)
    local = django_forms.ModelChoiceField(queryset=Time.objects.all(), label="Selecione o time local", required=False)
    data = django_forms.DateField(label="Data da partida", required=False)

class PartidaModelForm(ModelForm):
    class Meta:
        model = Partida
        fields = ["local", "visitante", "data"]

class PolemicaModelForm(ModelForm):
    class Meta:
        model = DeclaracaoArbitro
        fields = ["descricao","data","peso"]

class PolemicaForm(django_forms.Form):
    descricao = django_forms.CharField(widget=django_forms.Textarea, max_length=400, label="Descrição:")
    data = django_forms.DateField(label="Data do ocorrido:", required=False)
    peso = django_forms.IntegerField(label="Peso:")

class PolemicaVPModelForm(ModelForm):
    class Meta:
        model = VidapubliArbitro
        fields = ["descricao","data","peso" ]

class PolemicaVPForm(django_forms.Form):
    descricao = django_forms.CharField(widget=django_forms.Textarea, max_length=400, label="Descrição:")
    data = django_forms.DateField(label="Data do ocorrido:", required=False)
    peso = django_forms.IntegerField(label="Peso:")

class DenunciasModelForm(ModelForm):
    class Meta:
        model = DenunciaArbitro
        fields = ["descricao","data","peso" ]

class DenunciasForm(django_forms.Form):
    descricao = django_forms.CharField(widget=django_forms.Textarea, max_length=400, label="Descrição:")
    data = django_forms.DateField(label="Data do ocorrido:", required=False)
    peso = django_forms.IntegerField(label="Peso:")

class PapeladaModelForm(ModelForm):
    class Meta:
        model = DocumentoArbitro
        fields = ["descricao","data","peso" ]

class PapeladaForm(django_forms.Form):
    descricao = django_forms.CharField(widget=django_forms.Textarea, max_length=400, label="Descrição:")
    data = django_forms.DateField(label="Data do ocorrido:", required=False)
    peso = django_forms.IntegerField(label="Peso:")

