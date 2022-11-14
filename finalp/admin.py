from django.contrib import admin
from .models import *

#Ingresar los modelos para poder manejarlos desde el panel de admin

admin.site.register(Consolas)
admin.site.register(Juegos)
admin.site.register(Accesorios)
