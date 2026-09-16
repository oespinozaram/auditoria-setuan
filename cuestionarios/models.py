from django.db import models

class Entrevista(models.Model):
    PERFIL_CHOICES = [
        ('ADMIN', 'Personal Administrativo / Ventanilla'),
        ('TECNICO', 'Infraestructura y Sistemas'),
        ('TRANSPARENCIA', 'Unidad de Transparencia / Jurídico'),
        ('FINANZAS', 'Finanzas / Nómina / Tesorería'),
    ]

    entrevistado = models.CharField(max_length=150)
    cargo = models.CharField(max_length=120, null=True, blank=True)
    area = models.CharField(max_length=100, null=True, blank=True)
    perfil = models.CharField(max_length=20, choices=PERFIL_CHOICES, default='ADMIN')
    fecha = models.DateTimeField(auto_now_add=True)
    observaciones_generales = models.TextField(blank=True)

    def __str__(self):
        return f"{self.entrevistado} ({self.get_perfil_display()}) - {self.area}"


# Bloque A: Personal Administrativo y Flujo Operativo
class EvaluacionAdministrativa(models.Model):
    entrevista = models.OneToOneField(Entrevista, on_delete=models.CASCADE, related_name='eval_administrativa')
    gestion_accesos = models.TextField(verbose_name="Asignación y uso compartido de credenciales")
    flujo_informacion = models.TextField(verbose_name="Canales de envío de padrones/datos sensibles (WhatsApp, USB, correo)")
    equipos_computo = models.TextField(verbose_name="Uso de equipos institucionales vs. personales (BYOD)")
    respuesta_incidentes = models.TextField(verbose_name="Protocolo ante fallas, bloqueos o sospecha de virus")
    bajas_laborales = models.TextField(verbose_name="Tiempo de revocación de accesos tras renuncia o despido")


# Bloque B y C: Perfil Técnico, Arquitectura y Continuidad
class EvaluacionTecnica(models.Model):
    entrevista = models.OneToOneField(Entrevista, on_delete=models.CASCADE, related_name='eval_tecnica')
    inventario_software = models.TextField(verbose_name="Sistemas principales y aplicaciones legacy sin soporte")
    bases_datos = models.TextField(verbose_name="Motores de base de datos y control de usuarios privilegiados")
    interconexion_apis = models.TextField(verbose_name="Integraciones entre sistemas y exposición de endpoints")
    despliegues_mantenimiento = models.TextField(verbose_name="Procesos de actualización y entornos de prueba")
    monitoreo_logs = models.TextField(verbose_name="Trazabilidad y registro de eventos ante fugas de información")
    estrategia_respaldos = models.TextField(verbose_name="Frecuencia de backups de bases de datos y archivos")
    aislamiento_backups = models.TextField(verbose_name="Resguardo físico/lógico y protección contra ransomware")
    pruebas_recuperacion = models.TextField(verbose_name="Historial y pruebas de restauración ante caídas")

    
# Bloque Específico: Transparencia, Datos Sensibles y Jurídico (Nayarit)
class EvaluacionTransparencia(models.Model):
    entrevista = models.OneToOneField(Entrevista, on_delete=models.CASCADE, related_name='eval_transparencia')
    politica_clasificacion = models.TextField(verbose_name="Políticas alineadas a la Ley de Transparencia de Nayarit")
    versiones_publicas_testado = models.TextField(verbose_name="Procedimiento y herramientas para testar datos (RFC, CURP, firmas)")
    aviso_privacidad = models.TextField(verbose_name="Presencia y difusión de aviso de privacidad integral")
    canales_recepcion_pnt = models.TextField(verbose_name="Manejo y almacenamiento de solicitudes de la PNT en equipos locales")
    archivo_digital_nube = models.TextField(verbose_name="Resguardo de expedientes digitales en nubes (Drive/Dropbox) y cuentas máster")
