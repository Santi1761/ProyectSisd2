from django.shortcuts import render
from rest_framework import generics
from .models import Contract, DeliveryCertificate
from .serializers import ContractSerializer, DeliveryCertificateSerializer

class ContractListView(generics.ListCreateAPIView):
    queryset = Contract.objects.all()
    serializer_class = ContractSerializer

class DeliveryCertificateListView(generics.ListCreateAPIView):
    queryset = DeliveryCertificate.objects.all()
    serializer_class = DeliveryCertificateSerializer
