from django.urls import path
from .views import menu, catalogo, subir_partitura, actualizar_partitura, eliminar_partitura, visualizar_partitura

urlpatterns = [
    path('menu/', menu, name='menu'),
    path('catalogo/', catalogo, name='catalogo'),
    path('subir_partitura/', subir_partitura, name='subir_partitura'),
    path('actualizar_partitura/<int:partitura_id>/', actualizar_partitura, name='actualizar_partitura'),
    path('eliminar_partitura/<int:partitura_id>/', eliminar_partitura, name='eliminar_partitura'),
    path('visualizar_partitura/<int:partitura_id>/', visualizar_partitura, name='visualizar_partitura'),
]