from django.shortcuts import render
from .models import Usuario,Vehiculo,Alquiler

def index(request):
    return render(request,'carsharing/index.html',{})

def signIn(request):
    return render(request,'carsharing/signIn.html',{})

def logIn(request):
    return render(request,'carsharing/logIn.html',{})

def perfil(request):
    usuario = getUsuario(3)
    list_vehiculos = getVehiculos(usuario.codigo)
    list_alquileres = getAlquileres([vehiculo.id for vehiculo in list_vehiculos])
    vehiculos = tuple(zip(list_vehiculos,list_alquileres))
    return render(request,'carsharing/profile.html',{"usuario":usuario,"vehiculos":vehiculos})

def singleProduct(request):
    return render(request,'carsharing/single-product.html',{})

def addCar(request):
    return render(request,'carsharing/addCar.html',{})

def rentACar(request):
    return render(request,'carsharing/rentAcar.html',{})

def getUsuario(codigo):
    return Usuario.objects.get(pk=codigo)
def getVehiculos(codigo_propietario):
    return Vehiculo.objects.filter(propietario_id=codigo_propietario)
def getAlquileres(vehiculos_ids):
    return  Alquiler.objects.filter(vehiculo_id__in=vehiculos_ids)