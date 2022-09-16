from django.contrib import admin
from django.urls import path
from privado.views import *
from SisArbitros.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name="url_index"),
    path('login/', login, name="url_login"),
    path('times/', times, name="url_times"),
    path('formTime/', formTime, name="url_formTime"),
    path('updateTime/<int:id>/', updateTime, name="url_updateTime"),
    path('deleteTime/<int:id>/', deleteTime, name="url_deleteTime"),
    path('conflitos/', conflitos , name="url_conflitos"),
    path('formConflito/', formConflito, name="url_formConflito"),
    path('updateConflito/<int:id>/', updateConflito, name="url_updateConflito"),
    path('deleteConflito/<int:id>/', deleteConflito, name="url_deleteConflito"),
    path('formCidade/', formCidade, name="url_formCidade"),
    path('cidades/', cidades, name="url_cidades"),
    path('updateCidade/<int:id>', updateCidade, name="url_updateCidade"),
    path('deleteCidade/<int:id>', deleteCidade, name="url_deleteCidade"),
    path('formArbitro/', formArbitro, name="url_formArbitro"),
    path('arbitros/', arbitros, name="url_arbitros"),
    path('updateArbitro/<int:id>', updateArbitro, name="url_updateArbitro"),
    path('deleteArbitro/<int:id>', deleteArbitro, name="url_deleteArbitro"),
    path('detalhamentoArbitro/<int:id>', detalhamentoArbitro, name="url_detalhamentoArbitro"),
    path('InfoAdicionais/<int:id>', InfoAdicionais, name="url_InfoAdicionais"),
    path('polemicas/', formPolemica, name="url_polemicas"),
    path('updatePolemica/<int:id>', updatePolemica, name="url_updatePolemica"),
    path('deletePolemica/<int:id>', deletePolemica, name="url_deletePolemica"),
    path('polemicasvp/', formPolemicaVP, name="url_polemicasvp"),
    path('updatePolemicaVP/<int:id>', updatePolemicaVP, name="url_updatePolemicaVP"),
    path('deletePolemicaVP/<int:id>', deletePolemicaVP, name="url_deletePolemicaVP"),
    path('Denuncias/', formDenuncias, name="url_denuncias"),
    path('updateDenuncias/<int:id>', updateDenuncias, name="url_updateDenuncias"),
    path('deleteDenuncias/<int:id>', deleteDenuncias, name="url_deleteDenuncias"),
    path('Papelada/', formPapelada, name="url_papelada"),
    path('updatePapelada/<int:id>', updatePapelada, name="url_updatePapelada"),
    path('deletePapelada/<int:id>', deletePapelada, name="url_deletePapelada"),
    path('sorteio/', sorteio, name="url_sorteio"),

]