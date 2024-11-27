from django import forms
from .models import Contract, DeliveryCertificate

class ContractForm(forms.ModelForm):
    class Meta:
        model = Contract
        fields = ['contract_id', 'contract_number', 'start_date', 'end_date', 'monthly_value']

class DeliveryCertificateForm(forms.ModelForm):
    class Meta:
        model = DeliveryCertificate
        fields = ['certificate_id', 'contract', 'delivery_date', 'notes']
