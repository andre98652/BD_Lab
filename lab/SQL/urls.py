from django.urls import path
from . import views

urlpatterns = [
    path('clientes/', views.cliente_list, name='cliente_list'),
    path('clientes/add/', views.cliente_add, name='cliente_add'),
    path('clientes/edit/<int:pk>/', views.cliente_edit, name='cliente_edit'),
    path('clientes/delete/<int:pk>/', views.cliente_delete, name='cliente_delete'),
]