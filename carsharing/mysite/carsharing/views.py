from django.http import HttpResponseRedirect
from django.shortcuts import render
from .models import Usuario,Vehiculo,Alquiler,Ciudad
from .forms import AddVehicle
def index(request):
    return render(request,'carsharing/index.html',{})

def signIn(request):
    return render(request,'carsharing/signIn.html',{})

def logIn(request):
    return render(request,'carsharing/logIn.html',{})

def perfil(request):
    usuario = getUsuario(3)

    if request.method == 'POST':
        form = AddVehicle(request.POST,request.FILES)

        if form.is_valid():
            ciudad = getCiudad(form.cleaned_data["ciudad"])
            descripcion = form.cleaned_data["descripcion"]
            marca = form.cleaned_data["marca"]
            modelo = form.cleaned_data["modelo"]
            año = form.cleaned_data["año"]
            precio = form.cleaned_data["precio"]
            foto = form.cleaned_data["foto"]

            vehiculo = Vehiculo(foto=foto,descripcion=descripcion,marca=marca,modelo=modelo,año=año,disponible=True,propietario=usuario,ciudad=ciudad)
            vehiculo.save()

            alquiler = Alquiler(vehiculo=vehiculo,precio=precio)
            alquiler.save()
            return HttpResponseRedirect("/perfil")

    list_vehiculos = getVehiculos(usuario.codigo)
    list_alquileres = reversed(getAlquileres([vehiculo.id for vehiculo in list_vehiculos]))
    vehiculos = tuple(zip(list_vehiculos,list_alquileres))
    return render(request,'carsharing/profile.html',{"usuario":usuario,"vehiculos":vehiculos})

def singleProduct(request):
    return render(request,'carsharing/single-product.html',{})

def addCar(request):
    form = AddVehicle()
    return render(request,'carsharing/addCar.html',{"form":form})

def rentACar(request):
    return render(request,'carsharing/rentAcar.html',{})

def getUsuario(codigo):
    return Usuario.objects.get(pk=codigo)
def getVehiculos(codigo_propietario):
    return Vehiculo.objects.filter(propietario_id=codigo_propietario)
def getAlquileres(vehiculos_ids):
    return  Alquiler.objects.filter(vehiculo_id__in=vehiculos_ids)
def getCiudad(nombre_ciudad):
    return Ciudad.objects.filter(nombre=nombre_ciudad)[0]