# rentals/views.py
from django.shortcuts import render
from rest_framework import generics
from .models import Contract, DeliveryCertificate
from .serializers import ContractSerializer, DeliveryCertificateSerializer

# API Views
class ContractListView(generics.ListCreateAPIView):
    queryset = Contract.objects.all()
    serializer_class = ContractSerializer

class DeliveryCertificateListView(generics.ListCreateAPIView):
    queryset = DeliveryCertificate.objects.all()
    serializer_class = DeliveryCertificateSerializer

# Views for Templates
def contract_list(request):
    contracts = Contract.objects.all()
    return render(request, 'rentals/contract_list.html', {'contracts': contracts})

def certificate_list(request):
    certificates = DeliveryCertificate.objects.all()
    return render(request, 'rentals/certificate_list.html', {'certificates': certificates})
