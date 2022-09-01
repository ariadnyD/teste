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
from django.contrib import admin
from django.urls import path
from privado.views import  time, createTime, updateTime, deleteTime, conflito, createConflito, updateConflito, deleteConflito

urlpatterns = [
    path('admin/', admin.site.urls),
    path('times/', time),
    path('adicionarTime/', createTime),
    path('updateTime/<int:id>/', updateTime, name="url_updateTime"),
    path('deleteTime/<int:id>/', deleteTime, name="url_deleteTime"),
    path('conflitos/', conflito),
    path('adicionarConflito/', createConflito),
    path('updateConflito/<int:id>/', updateConflito, name="url_updateConflito"),
    path('deleteConflito/<int:id>/', deleteConflito, name="url_deleteConflito"),
]