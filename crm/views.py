from django.shortcuts import render, get_object_or_404, redirect
from .models import Company, Contact, Opportunity, ProductService, Equipment
from django.http import HttpResponse

# Vista para listar todas las compañías
def company_list(request):
    companies = Company.objects.all()
    for company in companies:
        print(company.id)  # Check the ID of each company
    return render(request, 'crm/company_list.html', {'companies': companies})



# Vista para agregar una nueva compañía
def company_add(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        industry = request.POST.get('industry')
        address = request.POST.get('address')
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        country = request.POST.get('country')
        state = request.POST.get('state')
        company = Company.objects.create(
            name=name, industry=industry, address=address, phone=phone,
            email=email, country=country, state=state
        )
        return redirect('company_list')
    return render(request, 'crm/company_add.html')

# Vista para ver los detalles de una compañía
def company_detail(request, company_id):
    company = get_object_or_404(Company, nit=company_id)
    return render(request, 'crm/company_detail.html', {'company': company})

