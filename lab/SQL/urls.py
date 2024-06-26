from django.urls import path
from . import views

urlpatterns = [
    path('clientes/', views.gestion_clientes, name='gestion_clientes'),
    path('clientes/list/', views.cliente_list, name='cliente_list'),
    path('clientes/add/', views.cliente_add, name='cliente_add'),
    path('clientes/edit/<int:pk>/', views.cliente_edit, name='cliente_edit'),
    path('clientes/delete/<int:pk>/', views.cliente_delete, name='cliente_delete'),
    path('clientes/toggle_status/<int:pk>/', views.toggle_cliente_status, name='toggle_cliente_status'),
    path('estado_cliente/', views.estado_cliente_list, name='estado_cliente_list'),
    path('estado_cliente/add/', views.estado_cliente_add, name='estado_cliente_add'),
    path('estado_cliente/edit/<str:pk>/', views.estado_cliente_edit, name='estado_cliente_edit'),
    path('estado_cliente/delete/<str:pk>/', views.estado_cliente_delete, name='estado_cliente_delete'),
    path('tipo_cliente/', views.tipo_cliente_list, name='tipo_cliente_list'),
    path('tipo_cliente/add/', views.tipo_cliente_add, name='tipo_cliente_add'),
    path('tipo_cliente/edit/<str:pk>/', views.tipo_cliente_edit, name='tipo_cliente_edit'),
    path('tipo_cliente/delete/<str:pk>/', views.tipo_cliente_delete, name='tipo_cliente_delete'),
    path('personal/', views.gestion_personal, name='gestion_personal'),
    path('personal/list/', views.personal_list, name='personal_list'),
    path('personal/add/', views.personal_add, name='personal_add'),
    path('personal/edit/<int:pk>/', views.personal_edit, name='personal_edit'),
    path('personal/delete/<int:pk>/', views.personal_delete, name='personal_delete'),
    path('cargo_personal/', views.cargo_personal_list, name='cargo_personal_list'),
    path('cargo_personal/add/', views.cargo_personal_add, name='cargo_personal_add'),
    path('cargo_personal/edit/<int:pk>/', views.cargo_personal_edit, name='cargo_personal_edit'),
    path('cargo_personal/delete/<int:pk>/', views.cargo_personal_delete, name='cargo_personal_delete'),
    path('actividades/', views.gestion_actividades, name='gestion_actividades'),
    path('actividades/list/', views.actividad_list, name='actividad_list'),
    path('actividades/add/', views.actividad_add, name='actividad_add'),
    path('actividades/edit/<int:pk>/', views.actividad_edit, name='actividad_edit'),
    path('actividades/delete/<int:pk>/', views.actividad_delete, name='actividad_delete'),
    path('etapas_proyecto/', views.etapas_proyecto_list, name='etapas_proyecto_list'),
    path('etapas_proyecto/add/', views.etapas_proyecto_add, name='etapas_proyecto_add'),
    path('etapas_proyecto/edit/<int:pk>/', views.etapas_proyecto_edit, name='etapas_proyecto_edit'),
    path('etapas_proyecto/delete/<int:pk>/', views.etapas_proyecto_delete, name='etapas_proyecto_delete'),
    path('tiempos_reales/', views.tiempos_reales_list, name='tiempos_reales_list'),
    path('tiempos_reales/add/', views.tiempos_reales_add, name='tiempos_reales_add'),
    path('tiempos_reales/edit/<int:pk>/', views.tiempos_reales_edit, name='tiempos_reales_edit'),
    path('tiempos_reales/delete/<int:pk>/', views.tiempos_reales_delete, name='tiempos_reales_delete'),
    path('plantilla_actividades/', views.plantilla_actividades_list, name='plantilla_actividades_list'),
    path('plantilla_actividades/add/', views.plantilla_actividades_add, name='plantilla_actividades_add'),
    path('plantilla_actividades/edit/<int:pk>/', views.plantilla_actividades_edit, name='plantilla_actividades_edit'),
    path('plantilla_actividades/delete/<int:pk>/', views.plantilla_actividades_delete, name='plantilla_actividades_delete'),
    path('personal/toggle-status/<int:pk>/', views.toggle_personal_status, name='toggle_personal_status'),
    path('cargos_personal/toggle-status/<int:pk>/', views.toggle_cargo_personal_status, name='toggle_cargo_personal_status'),
    path('actividades/toggle/<int:pk>/', views.toggle_actividad_status, name='toggle_actividad_status'),
    path('etapas_proyecto/toggle/<int:pk>/', views.toggle_etapa_proyecto_status, name='toggle_etapa_proyecto_status'),
    path('tiempos_reales/toggle/<int:pk>/', views.toggle_tiempos_reales_status, name='toggle_tiempos_reales_status'),
    path('plantilla_actividades/toggle/<int:pk>/', views.toggle_plantilla_actividades_status, name='toggle_plantilla_actividades_status'),

]
