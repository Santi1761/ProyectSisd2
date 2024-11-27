from django.urls import path
from . import views

urlpatterns = [
    path('contracts/', views.ContractListView.as_view(), name='contract-list'),
    path('certificates/', views.DeliveryCertificateListView.as_view(), name='certificate-list'),
]
