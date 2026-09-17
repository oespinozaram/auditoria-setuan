from django.contrib import admin
from django.template.loader import render_to_string
from django.http import HttpResponse
from .models import ActividadDiaria, BitacoraQuincenal, Entregable


@admin.register(ActividadDiaria)
class ActividadDiariaAdmin(admin.ModelAdmin):
    list_display = ('fecha', 'categoria', 'horas_invertidas', 'descripcion_corta')
    list_filter = ('categoria', 'fecha')
    date_hierarchy = 'fecha'

    def descripcion_corta(self, obj):
        return obj.descripcion[:75] + '...' if len(obj.descripcion) > 75 else obj.descripcion
    descripcion_corta.short_description = 'Descripción'


@admin.register(BitacoraQuincenal)
class BitacoraQuincenalAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'fecha_inicio', 'fecha_fin', 'pagada')
    list_filter = ('pagada',)
    filter_horizontal = ('actividades',)
    actions = ['imprimir_bitacora']

    @admin.action(description='🖨️ Generar vista de impresión (PDF)')
    def imprimir_bitacora(self, request, queryset):
        # Tomamos la primera bitácora seleccionada
        bitacora = queryset.first()
        actividades = bitacora.actividades.all().order_by('fecha')

        # Calculamos el total de horas para el reporte
        total_horas = sum(act.horas_invertidas for act in actividades)

        html = render_to_string('admin/imprimir_bitacora.html', {
            'bitacora': bitacora,
            'actividades': actividades,
            'total_horas': total_horas,
        })
        return HttpResponse(html)


@admin.register(Entregable)
class EntregableAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'tipo', 'fecha_entrega')
    list_filter = ('tipo', 'fecha_entrega')
    search_fields = ('titulo',)
    filter_horizontal = ('bitacoras_relacionadas',)
