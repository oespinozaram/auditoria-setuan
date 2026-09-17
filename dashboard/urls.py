# dashboard/urls.py
from django.urls import path
from . import views

app_name = 'dashboard'

urlpatterns = [
    path('', views.dashboard_home, name='home'),
    path('entregable/<int:pk>/', views.entregable_detalle, name='entregable_detalle'),
    path('riesgos/', views.mapa_riesgos, name='mapa_riesgos'),
]