import json
from django.shortcuts import render, get_object_or_404
from django.db.models import Sum
from entregables.models import Entregable, ActividadDiaria, CategoriaTrabajo
from inventario.models import Activo
from mapeo_accesos.models import Acceso
from cuestionarios.models import EvaluacionTecnica, EvaluacionTransparencia, Entrevista

def dashboard_home(request):
    total_activos = Activo.objects.count()
    activos_criticos = Activo.objects.filter(es_critico=True).count()
    entrevistas_realizadas = Entrevista.objects.count()
    ultimos_entregables = Entregable.objects.all()[:5]

    # Calcular distribución de horas
    horas_por_categoria = ActividadDiaria.objects.values('categoria').annotate(total=Sum('horas_invertidas')).order_by(
        '-total')

    categorias_dict = dict(CategoriaTrabajo.choices)
    labels = []
    datos = []

    for item in horas_por_categoria:
        labels.append(categorias_dict.get(item['categoria'], item['categoria']))
        datos.append(float(item['total']))  # Float para que JSON lo acepte

    context = {
        'total_activos': total_activos,
        'activos_criticos': activos_criticos,
        'entrevistas_realizadas': entrevistas_realizadas,
        'ultimos_entregables': ultimos_entregables,
        'labels_grafica': json.dumps(labels),
        'datos_grafica': json.dumps(datos),
    }
    return render(request, 'dashboard/home.html', context)


def entregable_detalle(request, pk):
    entregable = get_object_or_404(Entregable, pk=pk)
    return render(request, 'dashboard/entregable_detalle.html', {'entregable': entregable})


def mapa_riesgos(request):
    # 1. Hardware/Sistemas Críticos
    activos_criticos = Activo.objects.filter(es_critico=True)

    # 2. Brechas Técnicas (Respaldos, Monitoreo)
    evaluaciones_tecnicas = EvaluacionTecnica.objects.all()

    # 3. Brechas de Cumplimiento (Ley de Transparencia Nayarit)
    evaluaciones_transparencia = EvaluacionTransparencia.objects.all()

    # 4. Privilegios Excesivos
    accesos_admin = Acceso.objects.filter(nivel_privilegio__icontains='admin')

    context = {
        'activos_criticos': activos_criticos,
        'evaluaciones_tecnicas': evaluaciones_tecnicas,
        'evaluaciones_transparencia': evaluaciones_transparencia,
        'accesos_admin': accesos_admin,
    }
    return render(request, 'dashboard/mapa_riesgos.html', context)

