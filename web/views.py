from django.shortcuts import render

from .models import Categoria, Productos

# Create your views here.

"""VISTAS PARA EL CATALOGO DE PRODUCTOS"""

def index(request):
    listaProductos = Productos.objects.all()
    print(listaProductos)
    context = {
        'productos':listaProductos
    }
    return render(request,'index.html')