from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('perfil', views.perfil, name='perfil'),
    path('single-product', views.singleProduct, name='single-product'),
]