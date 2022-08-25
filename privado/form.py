from dataclasses import fields
from django.forms import ModelForm
from privado.models import Time  

class TimeForm(ModelForm):
    class Meta:
        model = Time
        fields = ["codigo", "nome", "cidade"]