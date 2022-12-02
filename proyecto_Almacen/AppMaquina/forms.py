from django import forms

# creacion de formularios
class HerraFormulario(forms.Form):
    nombre = forms.CharField(max_length=50)
    cantidad = forms.IntegerField()
    ubicacion = forms.CharField()

class InsuFormulario(forms.Form):
    nombre = forms.CharField(max_length=50)
    cantidad = forms.IntegerField()
    ubicacion = forms.CharField()
    fecha_vence = forms.DateField()

class RepuFormulario(forms.Form):
    nombre = forms.CharField(max_length=50)
    maquina = forms.CharField(max_length=50)
    cantidad = forms.IntegerField()
    ubicacion = forms.CharField()

class TecFormulario(forms.Form):
    nombre = forms.CharField(max_length=50)
    email = forms.EmailField()