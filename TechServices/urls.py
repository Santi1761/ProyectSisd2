from django.contrib import admin
from django.urls import path, include
from .views import index

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'), 

    path('api/accounts/', include('accounts.urls')),
    path('api/crm/', include('crm.urls')),
    path('api/rentals/', include('rentals.urls')),
    path('api/inventory/', include('inventory.urls')),

    path('rentals/', include('rentals.urls')),
    path('inventory/', include('inventory.urls')),

    path('crm/', include('crm.urls')),
]
