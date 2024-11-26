from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from datetime import datetime
from .models import Company

# Listar compañías
def company_list(request):
    companies = Company.objects.all()
    return render(request, 'bases/company_list.html', {'companies': companies})

# Detalle de una compañía
def company_detail(request, pk):
    company = get_object_or_404(Company, pk=pk)
    return render(request, 'bases/company_detail.html', {'company': company})

# Crear una nueva compañía
def company_create(request):
    if request.method == "POST":
        name = request.POST.get("name")
        nit = request.POST.get("nit")
        industry = request.POST.get("industry")
        email = request.POST.get("email")
        state = request.POST.get("state")
        
        # Crear el objeto con una fecha manual
        Company.objects.create(
            name=name,
            nit=nit,
            industry=industry,
            email=email,
            state=state,
            creation_date=datetime.now()  # Asignar la fecha actual
        )
        return redirect('company_list')
    return render(request, 'bases/company_form.html')

# Editar una compañía
def company_edit(request, pk):
    company = get_object_or_404(Company, pk=pk)
    if request.method == 'POST':
        company.name = request.POST['name']
        company.nit = request.POST['nit']
        company.industry = request.POST['industry']
        company.email = request.POST['email']
        company.state = request.POST['state']
        company.save()
        return redirect('company_list')
    return render(request, 'bases/company_form.html', {'company': company})

# Eliminar una compañía
def company_delete(request, pk):
    company = get_object_or_404(Company, pk=pk)
    if request.method == 'POST':
        company.delete()
        return redirect('company_list')
    return render(request, 'bases/company_confirm_delete.html', {'company': company})
