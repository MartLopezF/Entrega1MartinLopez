from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name="home"),
    path('consolas/', consolas, name="consolas"),
    path('consolas/crear/', creacion_consolas, name="consolas-crear"),
    path('juegos/', juegos, name="juegos"),
    path('juegos/crear/', creacion_juego, name="juegos-crear"),
    path('juegos/buscar/', buscador, name="juegos-buscar"),
    path('juegos/buscar/resultados', resultado_busqueda, name="juegos-buscar-resultados"),
    path('accesorios/', accesorios, name="accesorios"),
    path('accesorios/crear/', creacion_accesorios, name="accesorios-crear"),

]
