from django.urls import path
from appcoder.views import index, Profesores, Estudiantes, Cursos
urlpatterns = [
    path("",index, name="Inicio"),
    path("Profesores/", Profesores, name="profesores"),
    path("Estudiantes/", Estudiantes, name="Estudiantes"),
    path("Curso/", Cursos, name="Cursos"),
]