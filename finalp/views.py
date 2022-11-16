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

def creacion_consolas(request):

    if request.method == "POST":
        nombre_consola = request.POST["consola"]
        marca = request.POST["marca"]
        lanzamiento = request.POST["fecha de lanzamiento"]
        precio = request.POST["precio"]

        consola = Consolas(nombre=nombre_consola, marca=marca, fecha_lanzamiento=lanzamiento, precio=precio)
        consola.save()

    return render(request, "finalp/consola_formulario.html")


def juegos(request):
    lista_juegos = Juegos.objects.all()
    datos = {
        'juegos': lista_juegos

    }

    return render(request, 'finalp/juegos.html', datos)

def creacion_juego(request):

    if request.method == "POST":
        nombre_juego = request.POST["juego"]
        lanzamiento = request.POST["fecha de lanzamiento"]
        categoria = request.POST["categoria"]
        precio = request.POST["precio"]

        juego = Juegos(nombre=nombre_juego, fecha_lanzamiento=lanzamiento, categoria=categoria, precio=precio)
        juego.save()

    return render(request, "finalp/juego_formulario.html")

def accesorios(request):
    lista_accesorios = Accesorios.objects.all()
    datos = {
        'accesorios': lista_accesorios

    }

    return render(request, 'finalp/accesorios.html', datos)

def creacion_accesorios(request):

    if request.method == "POST":
        nombre_accesorio = request.POST["accesorio"]
        marca = request.POST["marca"]
        compatibilidad = request.POST["compatibilidad"]
        precio = request.POST["precio"]

        accesorio = Accesorios(nombre=nombre_accesorio, marca=marca, compatibilidad=compatibilidad, precio=precio)
        accesorio.save()

    return render(request, "finalp/accesorio_formulario.html")


def buscador(request):

    return render(request, "finalp/buscar.html")


def resultado_busqueda(request):
    nombre_juego = request.GET["nombre_juego"]
    juegos = Juegos.objects.filter(nombre__icontains=nombre_juego)

    return render(request, "finalp/resultado_busqueda.html", {"juegos": juegos})