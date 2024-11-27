# rentals/views.py
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic.edit import CreateView
from rest_framework import generics
from .models import Contract, DeliveryCertificate
from .serializers import ContractSerializer, DeliveryCertificateSerializer
from .forms import ContractForm, DeliveryCertificateForm

# API Views
class ContractListView(generics.ListCreateAPIView):
    queryset = Contract.objects.all()
    serializer_class = ContractSerializer

class DeliveryCertificateListView(generics.ListCreateAPIView):
    queryset = DeliveryCertificate.objects.all()
    serializer_class = DeliveryCertificateSerializer

class ContractCreateView(CreateView):
    model = Contract
    fields = ['contract_id', 'contract_number', 'start_date', 'end_date', 'monthly_value']
    template_name = 'rentals/contract_create.html'
    success_url = '/rentals/contracts/'

    def form_valid(self, form):
        return super().form_valid(form)

class DeliveryCertificateCreateView(CreateView):
    model = DeliveryCertificate
    fields = ['certificate_id', 'contract', 'delivery_date', 'notes']
    template_name = 'rentals/certificate_create.html'
    success_url = '/rentals/certificates/'

    def form_valid(self, form):
        return super().form_valid(form)

def contract_create(request):
    if request.method == 'POST':
        form = ContractForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('contract-list')
    else:
        form = ContractForm()
    return render(request, 'rentals/contract_create.html', {'form': form})

def contract_list(request):
    contracts = Contract.objects.all()
    return render(request, 'rentals/contract_list.html', {'contracts': contracts})

def delivery_certificate_create(request):
    if request.method == 'POST':
        form = DeliveryCertificateForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('certificate-list')
    else:
        form = DeliveryCertificateForm()
    return render(request, 'rentals/certificate_create.html', {'form': form})

def certificate_list(request):
    certificates = DeliveryCertificate.objects.all()
    return render(request, 'rentals/certificate_list.html', {'certificates': certificates})
