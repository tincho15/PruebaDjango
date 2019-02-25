from django.http import HttpResponse
from .models import Tarea, Persona
from django.shortcuts import render

# Create your views here.

def base_vista(request,*args,**kwargs):
	return render(request, "base.html", {})

def vista_tareas(request, *args, **kwargs):
    contexto_tareas = {
        'lista': Tarea.objects.all()
    }
    return render(request, 'tareas/showTareas.html', contexto_tareas)

def vista_personas(request, *args, **kwargs):
    contexto_personas = {
        'lista': Persona.objects.all()
    }
    return render(request, 'personas/showPersonas.html', contexto_personas)

