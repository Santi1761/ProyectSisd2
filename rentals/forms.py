# rentals/forms.py
from django import forms
from .models import Contract, DeliveryCertificate
from crm.models import Company  # Asegúrate de importar el modelo Company

class ContractForm(forms.ModelForm):
    class Meta:
        model = Contract
        fields = ['contract_id', 'contract_number', 'start_date', 'end_date', 'monthly_value', 'company']  # Añadir 'company'
    
    # Si necesitas establecer un valor predeterminado para company:
    company = forms.ModelChoiceField(queryset=Company.objects.all(), empty_label="Select a Company", required=True)


class DeliveryCertificateForm(forms.ModelForm):
    class Meta:
        model = DeliveryCertificate
        fields = ['certificate_id', 'contract', 'delivery_date', 'notes']
