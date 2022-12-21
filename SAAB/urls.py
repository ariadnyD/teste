from django.contrib import admin
from django.urls import path
from privado.views import *
from SisArbitros.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name="url_index"),
    path('search/', search, name="url_search"),

    path('login/', login_user, name="url_login"),
    path('sair/', sair, name="url_sair"),

    path('cadastrarUsuario/', formUsuario, name="url_cadastrarUsuario"),

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

    path('declaPolemicas/<int:id>', formPolemica, name="url_declaPolemicas"),
    path('updateDeclaPolemica/<int:ida>/<int:id>', updatePolemica, name="url_updateDeclaPolemica"),
    path('deleteDeclaPolemica/<int:ida>/<int:id>', deletePolemica, name="url_deleteDeclaPolemica"),

    path('polemicasvp/<int:id>', formPolemicaVP, name="url_polemicasvp"),
    path('updatePolemicaVP/<int:ida>/<int:id>', updatePolemicaVP, name="url_updatePolemicaVP"),
    path('deletePolemicaVP/<int:ida>/<int:id>', deletePolemicaVP, name="url_deletePolemicaVP"),

    path('Denuncias/<int:id>', formDenuncias, name="url_denuncias"),
    path('updateDenuncias/<int:ida>/<int:id>', updateDenuncias, name="url_updateDenuncias"),
    path('deleteDenuncias/<int:ida>/<int:id>', deleteDenuncias, name="url_deleteDenuncias"),

    path('Papelada/<int:id>', formPapelada, name="url_papelada"),
    path('updatePapelada/<int:ida>/<int:id>', updatePapelada, name="url_updatePapelada"),
    path('deletePapelada/<int:ida>/<int:id>', deletePapelada, name="url_deletePapelada"),

    path('sorteio/', sorteio, name="url_sorteio"),
    path('partidas/', inicioAdmin, name = "url_partida"),
    path('updatePartida/<int:id>', updatePartida, name = "url_updatePartida"),
    path('deletePartida/<int:id>', deletePartida, name = "url_deletePartida"),
    path('detalhamentoPartida/<int:id>', detalhamentoPartida, name = "url_detalhamentoPartida"),

    path('sobre/', sobre , name="url_sobre"),

]