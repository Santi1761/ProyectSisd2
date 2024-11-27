# crm/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('companies/', views.CompanyListView.as_view(), name='company-list'),
    path('contacts/', views.ContactListView.as_view(), name='contact-list'),
]
