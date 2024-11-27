# rentals/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('contracts/', views.contract_list, name='contract-list'),  # Ver contratos
    path('certificates/', views.certificate_list, name='certificate-list'),  # Ver actas
]
