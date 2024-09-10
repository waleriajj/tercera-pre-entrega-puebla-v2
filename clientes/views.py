from django.shortcuts import render, redirect
from .forms import CiudadForm, LugarForm, ProductoForm  # Importar los forms
from .models import lugar, ciudad, producto  # Importar los modelos correspondientes
from django.db.models import Q  # Importar Q para realizar las búsquedas

def home(request):
    query = request.GET.get('q')  # Obtener el valor buscado
    lugares = []
    ciudades = []
    productos = []

    # Si se ha enviado una búsqueda, filtra los resultados
    if query:
        # Buscar en el modelo Lugar (en nombre, direccion, ciudad)
        lugares = lugar.objects.filter(
            Q(nombre__icontains=query) | Q(direccion__icontains=query) | Q(ciudad__icontains=query)
        )

        # Buscar en el modelo Ciudad (en el nombre del país y de la ciudad)
        ciudades = ciudad.objects.filter(
            Q(ciudad__icontains=query) | Q(codigo_postal__icontains=query)
        )

        # Buscar en el modelo Producto (nombre, codigo, ciudad)
        productos = producto.objects.filter(
            Q(nombre_producto__icontains=query) | Q(codigo_producto__icontains=query) | Q(categoria__icontains=query)
        )

    context = {
        'query': query,
        'lugares': lugares,
        'ciudades': ciudades,
        'productos': productos,
    }

    return render(request, 'home.html', context)

def crear_ciudad(request):
    if request.method == 'POST':
        form = CiudadForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')  # Redirige a la URL home después de guardar
    else:
        form = CiudadForm()
    return render(request, 'crear_ciudad.html', {'form': form})

def crear_lugar(request):
    if request.method == 'POST':
        form = LugarForm(request.POST)
        if form.is_valid():
            form.save()  # Guarda los datos en la base de datos
            return redirect('home')  # Redirige a la URL home después de guardar
    else:
        form = LugarForm()
    return render(request, 'crear_lugar.html', {'form': form})

def crear_producto(request):
    if request.method == 'POST':
        form = ProductoForm(request.POST)
        if form.is_valid():
            form.save()  # Guarda los datos del formulario en la base de datos
            return redirect('home')  # Redirige a la URL home después de guardar
    else:
        form = ProductoForm()  # Crea un formulario vacío en solicitudes GET

    return render(request, 'crear_producto.html', {'form': form})
