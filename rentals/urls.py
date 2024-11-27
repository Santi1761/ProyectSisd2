# rentals/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('contracts/', views.contract_list, name='contract-list'),
    path('contracts/create/', views.contract_create, name='contract-create'), 
    path('certificates/', views.certificate_list, name='certificate-list'),
    path('certificates/create/', views.certificate_create, name='certificate-create'),
]
