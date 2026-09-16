from django.contrib import admin
from .models import Sistema, Acceso


class AccesoInline(admin.TabularInline):
    model = Acceso
    extra = 1


@admin.register(Sistema)
class SistemaAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'activo_hospedaje')
    search_fields = ('nombre',)
    inlines = [AccesoInline]
