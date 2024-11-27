# inventory/views.py
from django.shortcuts import render, redirect
from rest_framework import generics
from .models import Equipment, Category
from .serializers import EquipmentSerializer, CategorySerializer
from .forms import EquipmentForm, CategoryForm


class EquipmentListView(generics.ListCreateAPIView):
    queryset = Equipment.objects.all()
    serializer_class = EquipmentSerializer

class CategoryListView(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

def category_create(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('category-list')  
    else:
        form = CategoryForm()
    return render(request, 'inventory/category_create.html', {'form': form})

def category_list(request):
    categories = Category.objects.all()
    return render(request, 'inventory/category_list.html', {'categories': categories})

def equipment_create(request):
    if request.method == 'POST':
        form = EquipmentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('equipment-list')
    else:
        form = EquipmentForm()
    return render(request, 'inventory/equipment_create.html', {'form': form})

def equipment_list(request):
    equipment = Equipment.objects.all() 
    return render(request, 'inventory/equipment_list.html', {'equipment': equipment})