from django.db import models

# Create your models here.
class Usuario(models.Model):
    nombre = models.CharField(max_length=50)
    codigo = models.AutoField(auto_created=True, primary_key=True)
    password = models.CharField(max_length=20)
    email = models.EmailField()
    contacto = models.IntegerField()
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
    inicio = models.DateField()
    final = models.DateField()

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



