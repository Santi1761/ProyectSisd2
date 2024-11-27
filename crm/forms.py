# crm/forms.py
from django import forms
from .models import Company, Contact

class CompanyForm(forms.ModelForm):
    class Meta:
        model = Company
        fields = ['nit', 'name', 'industry', 'address', 'phone', 'email', 'country', 'state']

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['contact_id', 'company', 'first_name', 'last_name', 'position', 'phone', 'email', 'last_interaction_date']
