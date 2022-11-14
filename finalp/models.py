from django.db import models

#Ingresar los modelos a usar

class Consolas(models.Model):
    nombre = models.CharField(max_length=30)
    marca = models.CharField(max_length=20)
    fecha_lanzamiento = models.DateField()
    precio = models.IntegerField()

    def __str__(self):
        return self.nombre

class Juegos(models.Model):
    nombre = models.CharField(max_length=50)
    fecha_lanzamiento = models.DateField()
    categoria = models.CharField(max_length=50)
    precio = models.IntegerField()

    def __str__(self):
        return self.nombre

class Accesorios(models.Model):
    nombre = models.CharField(max_length=30)
    marca = models.CharField(max_length=20)
    compatibilidad = models.CharField(max_length=20)
    precio = models.IntegerField()

    def __str__(self):
        return self.nombre




