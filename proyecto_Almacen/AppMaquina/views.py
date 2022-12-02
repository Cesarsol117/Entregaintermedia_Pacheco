from django.shortcuts import render
from .models import *
from django.http import HttpResponse
from AppMaquina.forms import *

# Create your views here.
# def herramienta(request):
#     herramienta = Herramienta(nombre="llave inglesa", cantidad = 6, ubicacion = "a4")
#     herramienta.save()
#     cadena_texto = "herramienta guardada: "+herramienta.nombre+" "+"La cantidad es: "+ str(herramienta.cantidad)+" "+"su ubicacion es: "+ herramienta.ubicacion
#     return HttpResponse(cadena_texto)


def inicio(request):
    return render(request, "AppMaquina/inicio.html")

# def herramienta(request):
#     return render(request, "AppMaquina/Herramienta.html")
# formularios
def insumos(request):
    if request.method == 'POST':
        form=InsuFormulario(request.POST)
        if form.is_valid():
            informacion=form.cleaned_data
            print(informacion)
            nombre = informacion["nombre"]
            cantidad = informacion["cantidad"]
            ubicacion = informacion["ubicacion"]
            fecha_vence = informacion["fecha_vence"]

            insu = Insumos(nombre=nombre, cantidad=cantidad, ubicacion=ubicacion, fecha_vence=fecha_vence)
            insu.save()
            return render(request, "AppMaquina/inicio.html")
    else:
        formulario = InsuFormulario() 
        
    return render(request, "AppMaquina/insumos.html", {"form":formulario}) 

def repuestos(request):
    if request.method =='POST':
        form = RepuFormulario(request.POST)
        if form.is_valid():
            informacion=form.cleaned_data
            print(informacion)
            nombre= informacion["nombre"]
            maquina= informacion["maquina"]
            cantidad= informacion["cantidad"]
            ubicacion= informacion["ubicacion"]

            repu= Repuestos(nombre=nombre, maquina=maquina, cantidad=cantidad, ubicacion=ubicacion)
            repu.save()
            return render(request,"AppMaquina/inicio.html")
    else:
        formulario = RepuFormulario()
    return render(request, "AppMaquina/repuestos.html", {"form":formulario})

def tecnico(request):
    if request.method == 'POST':
        form = TecFormulario(request.POST)
        if form.is_valid():
            informacion=form.cleaned_data
            print(informacion)
            nombre = informacion["nombre"]
            email = informacion["email"]

            tecni = Tecnico(nombre=nombre, email=email)
            tecni.save()
            return render(request,"AppMaquina/inicio.html")
    else:
        formulario = TecFormulario()
    return render(request, "AppMaquina/tecnico.html", {"form":formulario})

def herramienta(request):
    if request.method == 'POST':
        form=HerraFormulario(request.POST)
        if form.is_valid():
            informacion=form.cleaned_data
            print(informacion)
            nombre = informacion["nombre"]
            cantidad = informacion["cantidad"]
            ubicacion = informacion["ubicacion"]

            herra = Herramienta(nombre=nombre, cantidad=cantidad, ubicacion=ubicacion)
            herra.save()
            return render(request, "AppMaquina/inicio.html")
    else:
        formulario = HerraFormulario() 

    return render(request, "AppMaquina/herramienta.html", {"form":formulario}) 
# busquedas

def busquedaherra(request):
    return render(request, "AppMaquina/busquedaherra.html")

def buscar(request):
    if request.GET["cosa"]:
        search = request.GET["cosa"]
        herramienta1 = Herramienta.objects.filter(nombre__icontains=search)
        return render(request, "AppMaquina/resultadosbusqueda.html", {"herramientas":herramienta1})
    else:
        return render(request, "AppMaquina/busquedaherra.html", {"mensaje": "no lleno nada"})

