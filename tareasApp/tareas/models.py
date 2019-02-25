from django.db import models

# Create your models here.

class Persona(models.Model):
	persona_id = models.AutoField(primary_key=True)
	nombre = models.CharField(max_length=30)
	email = models.EmailField(max_length=30)
	
	def __str__(self):
		return self.nombre

class Tarea(models.Model):
	titulo = models.CharField(max_length=60)
	descripcion = models.TextField()
	asignado = models.ForeignKey('Persona', null=True, blank=True, on_delete=models.SET_NULL)
	
	def __str__(self):
		return self.titulo


