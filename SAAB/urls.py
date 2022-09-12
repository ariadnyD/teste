"""SAAB URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from operator import index
from django.contrib import admin
from django.urls import path
from privado.views import *

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
    path('formArbitro/', formArbitro, name="url_formArbitro"),
    path('arbitros/', arbitros, name="url_arbitros"),
    path('updateArbitro/<int:id>', updateArbitro, name="url_updateArbitro"),
    path('deleteArbitro/<int:id>', deleteArbitro, name="url_deleteArbitro"),
    path('formCidade/', formCidade, name="url_formCidade"),
    path('cidades/', cidades, name="url_cidades"),
    path('updateCidade/<int:id>', updateCidade, name="url_updateCidade"),
    path('deleteCidade/<int:id>', deleteCidade, name="url_deleteCidade"),
]