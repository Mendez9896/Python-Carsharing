from django.contrib import admin
from .models import Vehiculo, Usuario,Ciudad,Alquiler

admin.site.site_header = 'Admin Carsharing'
# Register your models here.

class VehiculoAdmin(admin.ModelAdmin):
    list_display = ('propietario', 'foto','descripcion', 'marca', 'modelo', 'año','disponible','ciudad')

class UsuarioAdmin(admin.ModelAdmin):
    list_display = ('codigo','nombre','email','contacto','rol')

class AlquilerAdmin(admin.ModelAdmin):
    list_display = ('vehiculo','precio','inicio','final')

admin.site.register(Vehiculo,VehiculoAdmin)
admin.site.register(Usuario,UsuarioAdmin)
admin.site.register(Alquiler,AlquilerAdmin)
admin.site.register(Ciudad)
