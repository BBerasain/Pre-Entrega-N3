from django.http import HttpResponse
from django.shortcuts import render
from appcoder.models import Curso, Estudiante, Profesor

def index(request):
    return render(request, "index.html")
    
def Profesores(request):
    if request.method == "POST":
        nombre = request.POST.get("nombre")
        apellido = request.POST.get("apellido")
        email = request.POST.get("email")
        profesor = Profesor(nombre=nombre, apellido=apellido, email=email)
        profesor.save()
        return render(request, "index.html")
    return render(request, "profesores.html" )

def Estudiantes(request):
    if request.method == "POST":
        nombre = request.POST.get("nombre")
        apellido = request.POST.get("apellido")
        email = request.POST.get("email")
        estudiante = Estudiante(nombre=nombre, apellido=apellido, email=email)
        estudiante.save()
        return render(request, "index.html")
    return render(request, "Estudiantes.html" )

def Cursos(request):    
    if request.method == "POST":
        nombre = request.POST.get("curso")
        camada = request.POST.get("camada")
        curso = Curso(nombre=nombre, camada=camada)
        curso.save()
        return render(request, "index.html")       
    return render(request, "cursos.html")