from django.shortcuts import render
from .models import materia
# Create your views here.
def inicio_vista(request):
    ListadoMateria=materia.objects.all()
    return render(request,"gestionarMateria.html",{"lasmaterias":ListadoMateria})
