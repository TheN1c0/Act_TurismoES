from django.shortcuts import render, redirect

from .models import Alumno, Genero, Servicios
# Create your views here.

def index(request):
    Alumnos= Alumno.objects.all()
    context={"Alumnos":Alumnos}
    return render(request, 'turismo/index.html', context)

def listadoSQL(request):
    Alumnos= Alumno.objects.raw('SELECT * FROM turismo_alumno')
    context={"Alumnos":Alumnos}
    return render(request, 'turismo/listadoSQL.html', context)

def listar(request):
    Servicio= Servicios.objects.all()
    context={"Servicios":Servicio}
    return render(request, 'turismo/listar.html', context)

def registrarServicio(request):
        id = request.POST['idServicio']
        precio = request.POST['precioServicio']
        descripcion = request.POST['descripcionServicio']
        foto = request.FILES['fotoServicio']
        nuevo_servicio = Servicios(id= id, precio=precio, descripcion=descripcion, foto=foto)
        nuevo_servicio.save()

        return redirect('listar')