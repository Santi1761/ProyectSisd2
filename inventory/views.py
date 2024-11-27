# inventory/views.py
from django.shortcuts import render
from rest_framework import generics
from .models import Equipment, Category
from .serializers import EquipmentSerializer, CategorySerializer

# API Views
class EquipmentListView(generics.ListCreateAPIView):
    queryset = Equipment.objects.all()
    serializer_class = EquipmentSerializer

class CategoryListView(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

# Views for Templates
def equipment_list(request):
    equipment = Equipment.objects.all()  # Mostrar todos los equipos
    return render(request, 'inventory/equipment_list.html', {'equipment': equipment})

def category_list(request):
    categories = Category.objects.all()
    return render(request, 'inventory/category_list.html', {'categories': categories})
