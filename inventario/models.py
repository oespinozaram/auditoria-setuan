from django.db import models


class Activo(models.Model):
    TIPO_CHOICES = [('endpoint', 'Computadora/Endpoint'), ('server', 'Servidor'), ('red', 'Equipo de Red')]
    hostname = models.CharField(max_length=100)
    direccion_ip = models.GenericIPAddressField(null=True, blank=True)
    tipo = models.CharField(max_length=20, choices=TIPO_CHOICES)
    sistema_operativo = models.CharField(max_length=100)
    es_critico = models.BooleanField(default=False)
