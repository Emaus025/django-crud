from django.contrib import admin
from django.urls import path, include
from tasks import views

urlpatterns = [
    path('admin/', admin.site.urls),  # Panel de administración
#    path('', views.home, name='home'),  # Página de inicio
    path('signup/', views.signup, name='signup'),  # Registro de usuario
    path('signin/', views.signin, name='signin'),  # Inicio de sesión
    path('logout/', views.signout, name='logout'),  # Cerrar sesión
    path('tasks/', include('tasks.urls')),  # Incluir URLs de tasks
    path('partituras/', include('partituras.urls')),  # Incluir URLs de partituras
]
