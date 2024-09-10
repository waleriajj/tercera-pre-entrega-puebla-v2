from django.urls import path
from . import views

urlpatterns = [
    path('crear_producto/', views.crear_producto, name='crear_producto'), # Visualizacion template "crear_producto"
    path('crear_ciudad/', views.crear_ciudad, name='crear_ciudad'), # Visualizacion template "crear_ciudad"
    path('crear_lugar/', views.crear_lugar, name='crear_lugar'), # Visualizacion template "crear_lugar"
]
