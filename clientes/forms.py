from django import forms
from .models import lugar, ciudad, producto

# Form para los 3 models. con cada uno de losa tributos que tendra

class CiudadForm(forms.ModelForm):
    class Meta:
        model = ciudad
        fields = ['ciudad','codigo_postal']

class LugarForm(forms.ModelForm):
    class Meta:
        model = lugar
        fields = ['nombre', 'direccion', 'comuna']

class ProductoForm(forms.ModelForm):
    class Meta:
        model = producto
        fields = ['Nombre_producto', 'Codigo_producto', 'Categoria']
