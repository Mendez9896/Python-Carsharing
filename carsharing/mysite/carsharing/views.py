from django.shortcuts import render

def index(request):
    return render(request,'carsharing/index.html',{})

def signIn(request):
    return render(request,'carsharing/signIn.html',{})

def logIn(request):
    return render(request,'carsharing/logIn.html',{})

def perfil(request):
    return render(request,'carsharing/profile.html',{})

def singleProduct(request):
    return render(request,'carsharing/single-product.html',{})

def addCar(request):
    return render(request,'carsharing/addCar.html',{})

def rentACar(request):
    return render(request,'carsharing/rentAcar.html',{})