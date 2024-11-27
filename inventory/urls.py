# inventory/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('equipment/', views.equipment_list, name='equipment-list'),  # Ver equipos
    path('categories/', views.category_list, name='category-list'),  # Ver categorías
]
