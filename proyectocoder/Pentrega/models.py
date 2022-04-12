from django.db import models

class informacion(models.Model):
    nombre = models.CharField(max_length=40)
    edad = models.IntegerField()
    email = models.EmailField()


class peliculas(models.Model):
    nombrep = models.CharField(max_length=40)
    razonp = models.CharField(max_length=200)
    escenafavp = models.CharField(max_length=100)


class personaje(models.Model):
    pnombre = models.CharField(max_length=40)
    razon = models.CharField(max_length=200)
    identificado = models.CharField(max_length=200)
    escenafav = models.CharField(max_length=200)



    