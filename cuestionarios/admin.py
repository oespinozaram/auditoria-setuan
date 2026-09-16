from django.contrib import admin
from .models import (
    Entrevista,
    EvaluacionAdministrativa,
    EvaluacionTecnica,
    EvaluacionTransparencia,
)

class EvaluacionAdministrativaInline(admin.StackedInline):
    model = EvaluacionAdministrativa
    extra = 0

class EvaluacionTecnicaInline(admin.StackedInline):
    model = EvaluacionTecnica
    extra = 0

class EvaluacionTransparenciaInline(admin.StackedInline):
    model = EvaluacionTransparencia
    extra = 0

@admin.register(Entrevista)
class EntrevistaAdmin(admin.ModelAdmin):
    list_display = ('entrevistado', 'cargo', 'area', 'perfil', 'fecha')
    list_filter = ('perfil', 'area', 'fecha')
    search_fields = ('entrevistado', 'cargo', 'area')
    inlines = [
        EvaluacionAdministrativaInline,
        EvaluacionTecnicaInline,
        EvaluacionTransparenciaInline,
    ]
