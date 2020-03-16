from django.shortcuts import render

def index(request):
    return render(request,'carsharing/index.html',{})

def perfil(request):
    return render(request,'carsharing/profile.html',{})

def singleProduct(request):
    return render(request,'carsharing/single-product.html',{})