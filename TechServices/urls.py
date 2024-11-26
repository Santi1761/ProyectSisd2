from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('tests/', include('bases.urls')),
     path('crm/', include('crm.urls')),  
]
