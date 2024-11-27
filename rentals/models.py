# rentals/models.py
from django.db import models
from crm.models import Company

class Contract(models.Model):
    contract_id = models.CharField(max_length=20, primary_key=True)
    company = models.ForeignKey(Company, on_delete=models.CASCADE, related_name='contracts')
    contract_number = models.CharField(max_length=50, unique=True)
    start_date = models.DateField()
    end_date = models.DateField()
    monthly_value = models.DecimalField(max_digits=15, decimal_places=2)

    def __str__(self):
        return self.contract_number

class DeliveryCertificate(models.Model):
    certificate_id = models.CharField(max_length=20, primary_key=True)
    contract = models.ForeignKey(Contract, on_delete=models.CASCADE, related_name='certificates')
    delivery_date = models.DateField()
    notes = models.TextField(blank=True)

    def __str__(self):
        return self.certificate_id
