from django.contrib import admin
from .models import Activo


@admin.register(Activo)
class ActivoAdmin(admin.ModelAdmin):
    list_display = ('hostname', 'direccion_ip', 'tipo', 'sistema_operativo', 'es_critico')
    list_filter = ('tipo', 'es_critico')
    search_fields = ('hostname', 'direccion_ip', 'sistema_operativo')
