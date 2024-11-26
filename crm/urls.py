from django.urls import path
from . import views

urlpatterns = [
    path('', views.company_list, name='company_list'),
    path('company/add/', views.company_add, name='company_add'),
    path('company/<str:company_id>/', views.company_detail, name='company_detail'),
]
