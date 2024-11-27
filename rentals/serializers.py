# rentals/serializers.py
from rest_framework import serializers
from .models import Contract, DeliveryCertificate

class ContractSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contract
        fields = '__all__'

class DeliveryCertificateSerializer(serializers.ModelSerializer):
    class Meta:
        model = DeliveryCertificate
        fields = '__all__'
