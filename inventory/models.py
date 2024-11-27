# inventory/models.py
from django.db import models
from rentals.models import DeliveryCertificate

class Category(models.Model):
    category_id = models.CharField(max_length=20, primary_key=True)
    category_name = models.CharField(max_length=50, unique=True)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.category_name

class Equipment(models.Model):
    equipment_id = models.CharField(max_length=20, primary_key=True)
    certificate = models.ForeignKey(DeliveryCertificate, on_delete=models.CASCADE, related_name='equipment', null=True, blank=True)
    inventory_code = models.CharField(max_length=50, unique=True)
    description = models.TextField()
    active = models.BooleanField(default=True)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.inventory_code
