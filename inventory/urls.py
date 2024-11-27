from django.urls import path
from . import views

urlpatterns = [
    path('equipment/', views.EquipmentListView.as_view(), name='equipment-list'),
    path('categories/', views.CategoryListView.as_view(), name='category-list'),
]
