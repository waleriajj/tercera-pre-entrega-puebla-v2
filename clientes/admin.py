from django.contrib import admin
from .models import lugar, ciudad, producto

# Se agrega en la vista admin la visualizacion de los 3 models.
admin.site.register(lugar)
admin.site.register(ciudad)
admin.site.register(producto)


