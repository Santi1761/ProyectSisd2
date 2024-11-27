# crm/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('companies/', views.company_list, name='company-list'),
    path('companies/create/', views.company_create, name='company-create'),
    path('companies/edit/<str:nit>/', views.company_edit, name='company-edit'),
]
