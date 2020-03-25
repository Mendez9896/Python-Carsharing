from django import forms
import datetime
max_año = int(datetime.datetime.now().year) + 1
CIUDADES = (('La Paz', 'La Paz'),('Oruro', 'Oruro'),('Potosi','Potosi'),('Cochabamba','Cochabamba'),('Tarija','Tarija'),('Chuquisaca','Chuquisaca'),('Santa Cruz','Santa Cruz'),('Beni','Beni'),('Pando','Pando'),)


class AddVehicle(forms.Form):
    foto = forms.ImageField(allow_empty_file=True,widget = forms.FileInput(attrs = {'onchange' : "readURL(this);"}))
    descripcion = forms.CharField()
    marca = forms.CharField()
    modelo = forms.CharField()
    año = forms.IntegerField(min_value=1980, max_value=max_año)
    precio = forms.IntegerField()
    ciudad = forms.ChoiceField(choices=CIUDADES)

class EditUser(forms.Form):
    nombre = forms.CharField()
    apellido = forms.CharField()
    email = forms.EmailField()
    contacto = forms.CharField()

class EditVehiculo(forms.Form):
    id = forms.IntegerField(widget=forms.HiddenInput())
    foto = forms.ImageField(required=False,allow_empty_file=True, widget=forms.FileInput(attrs={'onchange': "readURL(this);"}))
    descripcion = forms.CharField()
    precio = forms.IntegerField()
    disponible = forms.BooleanField(required=False)
    ciudad = forms.ChoiceField(choices=CIUDADES)
class DeleteVehiculo(forms.Form):
    id = forms.IntegerField(widget=forms.HiddenInput())

class AddUser(forms.Form):
    nombre = forms.CharField()
    apellido = forms.CharField()
    usuario = forms.CharField()
    email = forms.EmailField()
    contacto = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

class DateInput(forms.DateInput):
    input_type = 'date'

class RentCar(forms.Form):
    inicio = forms.DateField(widget=DateInput)
    fin = forms.DateField(widget=DateInput)

