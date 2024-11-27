# crm/views.py
from rest_framework import generics
from .models import Company, Contact
from .serializers import CompanySerializer, ContactSerializer

class CompanyListView(generics.ListCreateAPIView):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer

class ContactListView(generics.ListCreateAPIView):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer
