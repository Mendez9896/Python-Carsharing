from django.urls import path

from . import views

urlpatterns = [
    path('index', views.index, name='index'),
    path('sign-in', views.signIn, name='sign-in'),
    path('', views.logIn, name='log-in'),
    path('perfil', views.perfil, name='perfil'),
    path('single-product/<str:pk>/', views.singleProduct, name='single-product'),
    path('add-car', views.addCar, name='add-car'),
    path('rent-a-car/<str:pk>/', views.rentACar, name='rent-a-car'),
    path('log-out',views.logOut,name='log-out'),
    path('rentingCar/<str:pk>',views.rentingCar,name='renting-car'),
    path('editar-user', views.editUser, name='editar-user'),
    path('editar-vehicle', views.editVehicle, name='editar-vehicle'),
    path('dismissWarning',views.dismissWarning,name='dismissWarning'),
    path('payment-process',views.paymentProcess,name='paymentProcess'),
    path('done', views.payment_done, name='done'),
    path('canceled', views.payment_canceled, name='canceled'),

]

