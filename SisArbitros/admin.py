from django.contrib import admin
from .models import Usuario, Cidade, Time, Arbitro, VidapubliArbitro, DeclaracaoArbitro, DenunciaArbitro, DocumentoArbitro, Partida, Conflito

admin.site.register(Usuario)
admin.site.register(Cidade)
admin.site.register(Time)
admin.site.register(Arbitro)
admin.site.register(VidapubliArbitro)
admin.site.register(DeclaracaoArbitro)
admin.site.register(DenunciaArbitro)
admin.site.register(DocumentoArbitro)
admin.site.register(Partida)
admin.site.register(Conflito)
# Register your models here.
