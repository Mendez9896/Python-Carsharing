from django.db import models

# Create your models here.
from setuptools.command.upload import upload


class Usuario(models.Model):
    codigo = models.AutoField(auto_created=True, primary_key=True)
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    usuario = models.CharField(max_length=50)
    email = models.EmailField()
    contacto = models.CharField(max_length=50)
    password = models.CharField(max_length=20)
    rol = models.BooleanField()

    def __str__(self):
        return str(self.codigo)

    class Meta:
        verbose_name_plural = "Usuarios"


class Ciudad(models.Model):
    nombre = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name_plural = "Ciudades"

class Vehiculo(models.Model):
    foto = models.ImageField(blank=True,null=True)
    propietario = models.ForeignKey(Usuario,on_delete=models.CASCADE)
    descripcion = models.TextField()
    marca = models.CharField(max_length=50)
    modelo = models.CharField(max_length=50)
    año = models.IntegerField()
    disponible = models.BooleanField()
    ciudad = models.ForeignKey(Ciudad,on_delete=models.CASCADE)

    def __str__(self):
        return self.marca+' '+self.modelo

    class Meta:
        verbose_name_plural = "Vehiculos"

class Alquiler(models.Model):
    vehiculo = models.ForeignKey(Vehiculo,on_delete=models.CASCADE)
    precio = models.IntegerField()
    inicio = models.DateField(blank=True,null=True)
    final = models.DateField(blank=True,null=True)
    cliente = models.ForeignKey(Usuario,on_delete=models.CASCADE,blank=True,null=True)

    def __str__(self):
        return str(self.vehiculo)

    class Meta:
        verbose_name_plural = "Alquileres"

class Pago(models.Model):
    codigo = models.IntegerField()
    precio = models.IntegerField()
    numeroTarjeta = models.IntegerField()
    tipoTarjeta = models.TextField()
    class Meta:
        verbose_name_plural = "Pagos"


class Propietario(models.Model):
    codigo = models.IntegerField()
    class Meta:
        verbose_name_plural = "Propietarios"



