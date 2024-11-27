from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/accounts/', include('accounts.urls')),
    path('api/crm/', include('crm.urls')),
    path('api/rentals/', include('rentals.urls')),
    path('api/inventory/', include('inventory.urls')),
]
