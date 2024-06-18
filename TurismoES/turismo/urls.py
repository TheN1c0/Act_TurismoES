from django.urls import path
from . import views
from django.shortcuts import redirect

urlpatterns = [path('index', views.index, name='index'),path('listadoSQL', views.listadoSQL, name='listadoSQL'), path('listar', views.listar, name='listar'), path('registrarServicio', views.registrarServicio,  name='registrarServicio'),path('',views.index, name='index'),]