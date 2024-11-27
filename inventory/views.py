from django.shortcuts import render
from rest_framework import generics
from .models import Equipment, Category
from .serializers import EquipmentSerializer, CategorySerializer

class EquipmentListView(generics.ListCreateAPIView):
    queryset = Equipment.objects.all()
    serializer_class = EquipmentSerializer

class CategoryListView(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
