from django import forms
from .models import Equipment, Category

class EquipmentForm(forms.ModelForm):
    class Meta:
        model = Equipment
        fields = ['inventory_code', 'description', 'category', 'active']

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['category_id', 'category_name', 'description']
