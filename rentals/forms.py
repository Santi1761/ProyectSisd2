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

from django import forms

class RentalProductForm(forms.Form):
    product_name = forms.ChoiceField(choices=[], required=True, label="Select Product")

    def __init__(self, *args, **kwargs):
        products = kwargs.pop('products', [])  # Recibe los productos como argumento
        super().__init__(*args, **kwargs)
        
        # Configurar las opciones del ChoiceField con los productos de PostgreSQL
        self.fields['product_name'].choices = [
            (product.inventory_code, f'{product.inventory_code} - {product.description}')
            for product in products
        ]


 