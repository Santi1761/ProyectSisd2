from django.contrib import admin

from .models import Company

@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    list_display = ('nit', 'name', 'industry', 'email', 'state')
    search_fields = ('name', 'nit')