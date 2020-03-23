from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render
from .models import Usuario,Vehiculo,Alquiler,Ciudad
from .forms import AddVehicle, AddUser,EditUser
from django.db.models import Q

def logOut(request):
    request.session['code']=-1
    return render(request,'carsharing/logIn.html',{})

def index(request):   
    if request.method=="POST":
        usuario=request.POST["usuario"]
        password=request.POST["password"]
        user=Usuario.objects.filter(usuario=usuario,password=password)
        if len(user)==0:
            return HttpResponseRedirect("/")
        else:
            request.session['code']=user[0].codigo
            return HttpResponseRedirect("/index")
    else:  
        if 'code' in request.session and request.session['code']!=-1:
            query = request.GET.get("buscar")
            if query:
                queryset = Vehiculo.objects.filter(
                    Q(descripcion__icontains = query) |
                    Q(marca__icontains = query) |
                    Q(modelo__icontains = query)  
                ).distinct()
            else:
                queryset = Vehiculo.objects.all()
            context = {
                "oject_list": queryset
            }
            return render(request,'carsharing/index.html',context)
        else:
            return HttpResponseRedirect("/")

def signIn(request):
    return render(request,'carsharing/signIn.html',{})

def logIn(request):
    if request.method=="POST":
        form = AddUser(request.POST)
        if form.is_valid():
            nombre = form.cleaned_data["nombre"]
            apellido = form.cleaned_data["apellido"]
            usuario = form.cleaned_data["usuario"]
            email = form.cleaned_data["email"]
            contacto = form.cleaned_data["contacto"]
            password = form.cleaned_data["password"]
            password2 = form.cleaned_data["password2"]
            if password != password2:
                return HttpResponseRedirect("/sign-in")
            else:
                usuario=Usuario(nombre=nombre,apellido=apellido,usuario=usuario,email=email,contacto=contacto,password=password,rol=True)
                usuario.save()
        else:
            return HttpResponseRedirect("/sign-in")

    return render(request,'carsharing/logIn.html',{})

def perfil(request):
    if 'code' in request.session and request.session['code']!=-1:
        usuario = getUsuario(request.session['code'])

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
    if request.method == 'POST':
        form = EditUser(request.POST)
        if form.is_valid():
            usuario.nombre = form.cleaned_data['nombre']
            usuario.apellido = form.cleaned_data['apellido']
            usuario.contacto = form.cleaned_data['contacto']
            usuario.email = form.cleaned_data['email']
            usuario.save()
            return HttpResponseRedirect("/perfil")
    list_vehiculos = getVehiculos(usuario.codigo)
    list_alquileres = reversed(getAlquileres([vehiculo.id for vehiculo in list_vehiculos]))
    vehiculos = tuple(zip(list_vehiculos,list_alquileres))
    return render(request,'carsharing/profile.html',{"usuario":usuario,"vehiculos":vehiculos})
def editUser(request):
    if 'code' in request.session and request.session['code']!=-1:
        usuario = getUsuario(request.session['code'])
    form = EditUser(initial={'nombre': usuario.nombre,'apellido':usuario.apellido,'email':usuario.email,'contacto':usuario.contacto})
    return render(request,'carsharing/editar-user.html',{"form":form, "user":usuario})
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
