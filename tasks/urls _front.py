from django.urls import path
from . import views

urlpatterns = [
    path('menu', views.tasks_menu, name='tasks_menu'),  # Lista de tareas
    path('pendientes', views.tasks, name='tasks'),  # Lista de tareas
    path('completed/', views.tasks_completed, name='task_completed'),  # Tareas completadas
    path('create/', views.create_task, name='create_task'),  # Crear tarea
    path('<int:task_id>/', views.task_detail, name='task_detail'),  # Detalle de tarea
    path('<int:task_id>/complete/', views.complete_task, name='complete_task'),  # Completar tarea
    path('<int:task_id>/delete/', views.delete_task, name='delete_task'),  # Eliminar tarea
]
