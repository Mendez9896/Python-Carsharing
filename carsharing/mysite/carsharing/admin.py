from django.contrib import admin
from .models import Vehiculo, Usuario,Ciudad,Alquiler

admin.site.site_header = 'Admin Carsharing'
# Register your models here.


class VehiculoAdmin(admin.ModelAdmin):
    list_display = ('propietario', 'descripcion', 'marca', 'modelo', 'año','disponible','ciudad')


admin.site.register(Vehiculo,VehiculoAdmin)
admin.site.register(Usuario)
admin.site.register(Ciudad)
admin.site.register(Alquiler)