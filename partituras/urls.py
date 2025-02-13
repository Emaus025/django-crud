from django.urls import path
from . import views

urlpatterns = [
    path('catalogo/', views.catalogo, name='catalogo'),
    path('menu/', views.menu, name='menu'),
    path('subir/', views.subir_partitura, name='subir_partitura'),
    path('actualizar/<int:partitura_id>/', views.actualizar_partitura, name='actualizar_partitura'),
    path('eliminar/<int:partitura_id>/', views.eliminar_partitura, name='eliminar_partitura'),
    path('visualizar/<int:partitura_id>/', views.visualizar_partitura, name='visualizar_partitura'),
]
