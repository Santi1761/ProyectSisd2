from django.contrib import admin
from django.urls import path, include
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from .views import index

urlpatterns = [
    path('admin/', admin.site.urls),
     # Redirige la raíz al login
    path('', lambda request: redirect('login'), name='root'),

    # Asegura que solo usuarios autenticados puedan ver el index
    path('index/', login_required(index), name='index'),

    path('accounts/', include('accounts.urls')),
    path('crm/', include('crm.urls')),
    path('rentals/', include('rentals.urls')),
    path('inventory/', include('inventory.urls')),
]
