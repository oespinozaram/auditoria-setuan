from django.db import models
from inventario.models import Activo


class Sistema(models.Model):
    nombre = models.CharField(max_length=100)
    activo_hospedaje = models.ForeignKey(Activo, on_delete=models.SET_NULL, null=True)
    descripcion = models.TextField()


class Acceso(models.Model):
    sistema = models.ForeignKey(Sistema, on_delete=models.CASCADE)
    rol_o_usuario = models.CharField(max_length=100)
    nivel_privilegio = models.CharField(max_length=50) # Ej. Administrador, Lectura
    metodo_autenticacion = models.CharField(max_length=100)