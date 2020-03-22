from django import forms
import datetime
max_año = int(datetime.datetime.now().year) + 1
class AddVehicle(forms.Form):
    foto = forms.ImageField(allow_empty_file=True)
    descripcion = forms.CharField()
    marca = forms.CharField()
    modelo = forms.CharField()
    año = forms.IntegerField(min_value=1980, max_value=max_año)
    precio = forms.IntegerField()