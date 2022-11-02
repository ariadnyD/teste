from django.contrib import admin
from .models import *
from django.contrib.auth import admin as admin_auth_django
from privado.forms import UserChangeForm, UserCreationForm

@admin.register(Usuario)
class UsersAdmin(admin_auth_django.UserAdmin):
    form = UserChangeForm
    add_form = UserCreationForm
    model = Usuario
    fieldsets = admin_auth_django.UserAdmin.fieldsets + (
        ('tipo', {'fields': ('tipo',)}),
    )

admin.site.register(Cidade)
admin.site.register(Time)
admin.site.register(Arbitro)
admin.site.register(VidapubliArbitro)
admin.site.register(DeclaracaoArbitro)
admin.site.register(DenunciaArbitro)
admin.site.register(DocumentoArbitro)
admin.site.register(Partida)
admin.site.register(Conflito)
