from django.db import models


class CategoriaTrabajo(models.TextChoices):
    RED = 'RED', 'Reestructuración de Red'
    ACOSO = 'ACOSO', 'Triage y Acoso Digital'
    CUMPLIMIENTO = 'CUMPLIMIENTO', 'Normatividad y Datos'
    INFRA = 'INFRA', 'Infraestructura y Respaldos'
    OTROS = 'OTROS', 'Otros / Juntas'


class ActividadDiaria(models.Model):
    fecha = models.DateField()
    categoria = models.CharField(max_length=20, choices=CategoriaTrabajo.choices)
    descripcion = models.TextField(help_text="Descripción detallada de la tarea realizada hoy.")
    horas_invertidas = models.DecimalField(max_digits=4, decimal_places=1, default=8.0)

    class Meta:
        verbose_name_plural = "Actividades Diarias"
        ordering = ['-fecha']

    def __str__(self):
        return f"{self.fecha} - {self.get_categoria_display()}"


class BitacoraQuincenal(models.Model):
    """Respalda el pago por honorarios quincenales."""
    titulo = models.CharField(max_length=100, help_text="Ej: Primera Quincena Octubre 2026")
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField()
    actividades = models.ManyToManyField(ActividadDiaria, blank=True)
    pagada = models.BooleanField(default=False)

    class Meta:
        verbose_name_plural = "Bitácoras Quincenales"

    def __str__(self):
        return self.titulo


class ReporteMensual(models.Model):
    """Reporte breve: qué se hizo, qué se encontró, qué sigue."""
    mes_reportado = models.CharField(max_length=50, help_text="Ej: Mes 1 - Estabilización y respuesta inmediata")
    que_se_hizo = models.TextField(help_text="Resumen de actividades completadas.")
    que_se_encontro = models.TextField(help_text="Hallazgos relevantes o incidentes.")
    que_sigue = models.TextField(help_text="Próximos pasos para el siguiente mes.")
    bitacoras_relacionadas = models.ManyToManyField(BitacoraQuincenal, blank=True)

    class Meta:
        verbose_name_plural = "Reportes Mensuales"

    def __str__(self):
        return f"Reporte: {self.mes_reportado}"