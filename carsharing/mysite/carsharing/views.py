from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render
from .models import Usuario,Vehiculo,Alquiler,Ciudad
from .forms import AddVehicle, AddUser,EditUser,EditVehiculo,DeleteVehiculo, RentCar
from django.db.models import Q
from django.contrib import messages

def error404(request, exception):
    return HttpResponseRedirect("/")

def error500(request):
    return HttpResponseRedirect("/")

def dismissWarning(request):
    request.session['code']=0
    return HttpResponseRedirect("/")

def logOut(request):
    request.session['code']=-1
    return HttpResponseRedirect("/")

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
    form = AddUser()
    return render(request,'carsharing/signIn.html',{"form":form})

def logIn(request):
    if 'code' in request.session and request.session['code']==-1:
        messages.warning(request, 'Sesion cerrada')
    elif 'code' in request.session and request.session['code']>0:
        return HttpResponseRedirect("/index")
    if request.method=="POST":
        form = AddUser(request.POST)
        if form.is_valid():
            nombre = form.cleaned_data["nombre"]
            apellido = form.cleaned_data["apellido"]
            usuario = form.cleaned_data["usuario"]
            email = form.cleaned_data["email"]
            contacto = form.cleaned_data["contacto"]
            password = form.cleaned_data["password"]
            usuario=Usuario(nombre=nombre,apellido=apellido,usuario=usuario,email=email,contacto=contacto,password=password, rol=True)
            usuario.save()    
        else:
            return HttpResponseRedirect("/sign-in")
        
    return render(request,'carsharing/logIn.html',{})

def perfil(request):
    if 'code' in request.session and request.session['code']!=-1:
        usuario = getUsuario(request.session['code'])

    if request.method == 'POST':
        form = AddVehicle(request.POST,request.FILES)
        form2 = EditUser(request.POST)
        form3 = EditVehiculo(request.POST)
        form4 = DeleteVehiculo(request.POST)
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
        elif form2.is_valid():
            usuario.nombre = form2.cleaned_data['nombre']
            usuario.apellido = form2.cleaned_data['apellido']
            usuario.contacto = form2.cleaned_data['contacto']
            usuario.email = form2.cleaned_data['email']
            usuario.save()
            return HttpResponseRedirect("/perfil")
        elif form3.is_valid():
            vehiculo = Vehiculo.objects.get(pk=form3.cleaned_data["id"])
            vehiculo.ciudad = getCiudad(form3.cleaned_data["ciudad"])
            vehiculo.descripcion = form3.cleaned_data["descripcion"]
            vehiculo.disponible = form3.cleaned_data["disponible"]
            precio = form3.cleaned_data["precio"]
            foto = form3.cleaned_data["foto"]
            if foto:
                vehiculo.foto = foto
            alquiler = getAlquileres([form3.cleaned_data["id"]])[0]
            alquiler.precio = precio
            vehiculo.save()
            alquiler.save()
            return HttpResponseRedirect("/perfil")
        elif form4.is_valid():
            Vehiculo.objects.get(pk=form4.cleaned_data["id"]).delete()
    list_vehiculos = getVehiculos(usuario.codigo)
    list_alquileres = reversed(getAlquileres([vehiculo.id for vehiculo in list_vehiculos]))
    vehiculos = tuple(zip(list_vehiculos,list_alquileres))
    list_owned_alquileres = getAlquileresByClient(usuario)
    return render(request,'carsharing/profile.html',{"usuario":usuario,"vehiculos":vehiculos,"alquileres": list_owned_alquileres})

def editUser(request):
    if 'code' in request.session and request.session['code']!=-1:
        usuario = getUsuario(request.session['code'])
    form = EditUser(initial={'nombre': usuario.nombre,'apellido':usuario.apellido,'email':usuario.email,'contacto':usuario.contacto})
    return render(request,'carsharing/editar-user.html',{"form":form, "user":usuario})

def editVehicle(request):
    vehiculo_id = request.GET.get("vehicle")
    vehiculo = Vehiculo.objects.get(pk=vehiculo_id)
    alquiler = getAlquileres([vehiculo_id])[0]
    form = EditVehiculo(initial={'disponible':vehiculo.disponible,'id':vehiculo_id,'descripcion':vehiculo.descripcion,'precio':alquiler.precio,'ciudad':vehiculo.ciudad.nombre})
    formD = DeleteVehiculo(initial={'id':vehiculo_id})
    return render(request,'carsharing/editar-vehicle.html',{"form":form,"formD":formD,"foto":vehiculo.foto.url})

def singleProduct(request, pk):
    vehiculo = Vehiculo.objects.get(id = pk)
    context = {'vehiculo': vehiculo }
    return render(request,'carsharing/single-product.html',context)

def addCar(request):
    form = AddVehicle()
    return render(request,'carsharing/addCar.html',{"form":form})

def rentACar(request, pk):
    form = RentCar()
    vehiculo = Vehiculo.objects.get(id = pk)
    alquiler = Alquiler.objects.get(vehiculo = vehiculo)
    context = {'vehiculo': vehiculo, 'alquiler': alquiler, "form": form}
    return render(request,'carsharing/rentAcar.html',context)

def rentingCar(request, pk):
    inicio=request.POST['inicio']
    fin=request.POST['fin']
    vehiculo = Vehiculo.objects.get(id = pk)
    alquiler = Alquiler.objects.get(vehiculo = vehiculo)
    alquiler.inicio=inicio
    alquiler.final=fin
    alquiler.cliente=getUsuario(request.session['code'])
    vehiculo.disponible=False
    vehiculo.save()
    alquiler.save()
    return HttpResponseRedirect("/perfil")


def getUsuario(codigo):
    return Usuario.objects.get(pk=codigo)
def getVehiculos(codigo_propietario):
    return Vehiculo.objects.filter(propietario_id=codigo_propietario)
def getAlquileres(vehiculos_ids):
    return  Alquiler.objects.filter(vehiculo_id__in=vehiculos_ids)
def getAlquileresByClient(cliente):
    return Alquiler.objects.filter(cliente=cliente)
def getCiudad(nombre_ciudad):
    return Ciudad.objects.filter(nombre=nombre_ciudad)[0]
