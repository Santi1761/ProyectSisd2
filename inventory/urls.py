from django.urls import path
from . import views

urlpatterns = [
    path('equipment/', views.equipment_list, name='equipment-list'),
    path('categories/', views.category_list, name='category-list'),
    path('equipment/create/', views.equipment_create, name='equipment-create'),
    path('categories/create/', views.category_create, name='category-create'),
]
