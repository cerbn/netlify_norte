# api/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('agregar_venta/', views.agregar_venta, name='agregar_venta'),
    path('estado_seguimiento/', views.estado_seguimiento, name='estado_seguimiento'),
]
