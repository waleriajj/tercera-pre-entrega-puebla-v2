from django.contrib import admin
from django.urls import include, path
from clientes import views

urlpatterns = [
    path('admin/', admin.site.urls), # Visualizacion del administrador
    path('clientes/', include('clientes.urls')),  # Visualizacion clientes y sus models
    path('', views.home, name='home'),  # Visualizacion pagina principal
]


