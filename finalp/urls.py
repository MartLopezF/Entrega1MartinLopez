from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name="home"),
    path('consolas/', consolas, name="consolas"),
    path('juegos/', juegos, name="juegos"),
    path('accesorios/', accesorios, name="accesorios"),
]
