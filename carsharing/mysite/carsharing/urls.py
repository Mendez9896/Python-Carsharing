from django.urls import path

from . import views

urlpatterns = [
    path('index', views.index, name='index'),
    path('sign-in', views.signIn, name='sign-in'),
    path('', views.logIn, name='log-in'),
    path('perfil', views.perfil, name='perfil'),
    path('single-product/<str:pk>/', views.singleProduct, name='single-product'),
    path('add-car', views.addCar, name='add-car'),
    path('rent-a-car', views.rentACar, name='rent-a-car'),
    path('log-out',views.logOut,name='log-out'),
    path('dismissWarning',views.dismissWarning,name='dismissWarning')
    path('editar-user', views.editUser, name='editar-user')

]
