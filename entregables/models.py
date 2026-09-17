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
    titulo = models.CharField(max_length=100, help_text="Ej: Primera Quincena Octubre 2026")
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField()
    actividades = models.ManyToManyField(ActividadDiaria, blank=True)
    pagada = models.BooleanField(default=False)

    class Meta:
        verbose_name_plural = "Bitácoras Quincenales"

    def __str__(self):
        return self.titulo


# --- NUEVO MODELO CONSOLIDADO ---

class TipoEntregable(models.TextChoices):
    MENSUAL = 'MENSUAL', 'Reporte Mensual Breve'
    CHECKPOINT_M4 = 'CHECKPOINT_M4', 'Checkpoint Transición (Mes 4)'
    TRIMESTRAL = 'TRIMESTRAL', 'Revisión Trimestral (Mes 6, 9, 12)'
    ANUAL = 'ANUAL', 'Reporte Ejecutivo Consolidado (Mes 12)'


class Entregable(models.Model):
    titulo = models.CharField(max_length=150, help_text="Ej: Reporte Mensual 1 o Checkpoint Fase 1")
    tipo = models.CharField(max_length=20, choices=TipoEntregable.choices, default=TipoEntregable.MENSUAL)
    fecha_entrega = models.DateField()

    # Campos homologados para cubrir "Qué se hizo/Avances", "Hallazgos/Riesgos" y "Qué sigue/Ajustes"
    resumen_ejecutivo = models.TextField(verbose_name="Avances / Qué se hizo", blank=True)
    hallazgos_riesgos = models.TextField(verbose_name="Riesgos / Qué se encontró", blank=True)
    proximos_pasos = models.TextField(verbose_name="Ajuste de prioridades / Qué sigue", blank=True)

    bitacoras_relacionadas = models.ManyToManyField(BitacoraQuincenal, blank=True)

    class Meta:
        verbose_name_plural = "Entregables y Reportes"
        ordering = ['-fecha_entrega']

    def __str__(self):
        return f"{self.get_tipo_display()} - {self.titulo}"
