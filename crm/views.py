# crm/views.py
from rest_framework import generics
from .models import Company, Contact
from .serializers import CompanySerializer, ContactSerializer
from django.shortcuts import get_object_or_404, render, redirect
from .forms import CompanyForm

class CompanyListView(generics.ListCreateAPIView):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer

class ContactListView(generics.ListCreateAPIView):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer

def company_list(request):
    companies = Company.objects.all()
    return render(request, 'crm/company_list.html', {'companies': companies})

def company_create(request):
    if request.method == 'POST':
        form = CompanyForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('company-list')
    else:
        form = CompanyForm()
    return render(request, 'crm/company_create.html', {'form': form})

def company_edit(request, nit):
    company = get_object_or_404(Company, nit=nit)
    if request.method == 'POST':
        form = CompanyForm(request.POST, instance=company)
        if form.is_valid():
            form.save()
            return redirect('company-list')
    else:
        form = CompanyForm(instance=company)
    return render(request, 'crm/company_edit.html', {'form': form, 'company': company})

