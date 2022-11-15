from django.shortcuts import render
from .models import *


#Importar los modelos de .models
#Ingresar las vistas a usar

def home(request):
    
    return render(request, 'finalp/index.html')

def consolas(request):
    lista_consolas = Consolas.objects.all()
    datos = {
        'consolas': lista_consolas

    }

    return render(request, 'finalp/consolas.html', datos)

def juegos(request):
    lista_juegos = Juegos.objects.all()
    datos = {
        'juegos': lista_juegos

    }

    return render(request, 'finalp/juegos.html', datos)

def accesorios(request):
    lista_accesorios = Accesorios.objects.all()
    datos = {
        'accesorios': lista_accesorios

    }

    return render(request, 'finalp/accesorios.html', datos)

def creacion_juego(request):

    if request.method == "POST":
        nombre_juego = request.POST["juego"]
        lanzamiento = request.POST["fecha de lanzamiento"]
        categoria = request.POST["categoria"]
        precio = request.POST["precio"]

        juego = Juegos(nombre=nombre_juego, fecha_lanzamiento=lanzamiento, categoria=categoria, precio=precio)
        juego.save()

    return render(request, "finalp/juego_formulario.html")
