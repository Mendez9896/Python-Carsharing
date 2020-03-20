from django.db import models

# Create your models here.
class Usuario(models.Model):
    nombre = models.CharField(max_length=50)

class Ciudad(models.Model):
    nombre = models.CharField(max_length=50)

class Vehiculo(models.Model):
    idPropietario = models.ForeignKey(Usuario,on_delete=models.CASCADE)
    descripcion = models.TextField()
    marca = models.CharField(max_length=50)
    modelo = models.CharField(max_length=50)
    año = models.IntegerField()
    disponible = models.BooleanField()
    ciudad = models.ForeignKey(Ciudad,on_delete=models.CASCADE)

class Alquiler(models.Model):
    idVehiculo = models.ForeignKey(Vehiculo,on_delete=models.CASCADE)
    precio = models.IntegerField()
    inicio = models.DateField()
    final = models.DateField()
