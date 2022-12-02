from django.contrib import admin
from django.urls import path
from AppMaquina.views import *

urlpatterns = [
    
    path('', inicio, name = "inicio"),
    path('herramienta/', herramienta, name = "herramienta"),
    path('insumos/', insumos, name = "insumos"),
    path('repuestos/', repuestos, name = "repuestos"),
    path('tecnico/', tecnico, name = "tecnico"),
    # path('formulario/', herraFomulario, name = "herraFormulario"),
    path('busquedaherra/', busquedaherra, name = "busquedaherra"),
    path('buscar/', buscar, name = "buscar"),
]