# rentals/views.py
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic.edit import CreateView
from rest_framework import generics
from .models import Contract, DeliveryCertificate
from .serializers import ContractSerializer, DeliveryCertificateSerializer
from .forms import ContractForm, DeliveryCertificateForm
from django.shortcuts import render, redirect
from .models import RentalProduct
from .forms import RentalProductForm
from django.contrib.auth.decorators import login_required
from datetime import datetime
from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404
from .models import RentalProduct
from django.utils.timezone import now

# API Views
class ContractListView(generics.ListCreateAPIView):
    queryset = Contract.objects.all()
    serializer_class = ContractSerializer

class DeliveryCertificateListView(generics.ListCreateAPIView):
    queryset = DeliveryCertificate.objects.all()
    serializer_class = DeliveryCertificateSerializer

class ContractCreateView(CreateView):
    model = Contract
    fields = ['contract_id', 'contract_number', 'start_date', 'end_date', 'monthly_value']
    template_name = 'rentals/contract_create.html'
    success_url = '/rentals/contracts/'

    def form_valid(self, form):
        return super().form_valid(form)

class DeliveryCertificateCreateView(CreateView):
    model = DeliveryCertificate
    fields = ['certificate_id', 'contract', 'delivery_date', 'notes']
    template_name = 'rentals/certificate_create.html'
    success_url = '/rentals/certificates/'

    def form_valid(self, form):
        return super().form_valid(form)

def contract_create(request):
    if request.method == 'POST':
        form = ContractForm(request.POST)
        if form.is_valid():
            contract = form.save(commit=False)  # No guardamos aún el contrato
            contract.company = form.cleaned_data['company']  # Asignar la empresa seleccionada
            contract.save()  # Ahora sí guardamos el contrato
            return redirect('contract-list')
    else:
        form = ContractForm()
    return render(request, 'rentals/contract_create.html', {'form': form})

def contract_list(request):
    contracts = Contract.objects.all()
    return render(request, 'rentals/contract_list.html', {'contracts': contracts})

def certificate_create(request):
    if request.method == 'POST':
        form = DeliveryCertificateForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('certificate-list')  # Redirige a la lista de actas de entrega
    else:
        form = DeliveryCertificateForm()
    return render(request, 'rentals/certificate_create.html', {'form': form})

def certificate_list(request):
    certificates = DeliveryCertificate.objects.all()
    return render(request, 'rentals/certificate_list.html', {'certificates': certificates})

from datetime import datetime

from django.shortcuts import render, redirect
from django.utils.timezone import now
from .forms import RentalProductForm
from .models import RentalProduct
from django.contrib.auth.decorators import login_required

from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import RentalProductForm
from inventory.models import Equipment  # Importar el modelo Equipment de la aplicación inventory
from mongoengine import Document
from datetime import datetime

@login_required
def rent_product(request):
    if request.method == 'POST':
        # Obtener los productos desde PostgreSQL (tabla Equipment)
        products = Equipment.objects.filter(active=True)  # Solo equipos activos (disponibles)

        # Crear el formulario con los productos obtenidos desde PostgreSQL
        form = RentalProductForm(request.POST, products=products)
        
        if form.is_valid():
            # Obtener el equipo seleccionado por el nombre (inventory_code)
            inventory_code = form.cleaned_data['product_name']
            
            # Consultar el producto seleccionado en PostgreSQL
            product = Equipment.objects.get(inventory_code=inventory_code)
            
            # Verificar si el producto está disponible
            if product.active:
                # Guardar el alquiler en MongoDB
                rental_product = RentalProduct(
                    product_name=product.inventory_code,  # Guardar el código del equipo
                    description=product.description,
                    user=request.user.username,  # Almacenar el nombre del usuario que alquila
                    rent_date=datetime.now()  # Fecha de alquiler
                )
                rental_product.save()  # Guardamos en MongoDB

                # Marcar el producto como no disponible (inactivo) en PostgreSQL
                product.active = False
                product.save()

                return redirect('rented-products')  # Redirigir a la lista de productos alquilados
            else:
                return render(request, 'rentals/rent_product.html', {
                    'form': form,
                    'error': 'Este producto ya está alquilado o no está disponible.'
                })
    else:
        # Obtener los productos disponibles desde PostgreSQL
        products = Equipment.objects.filter(active=True)  # Solo equipos activos
        form = RentalProductForm(products=products)

    return render(request, 'rentals/rent_product.html', {'form': form})




@login_required
def rented_products(request):
    # Obtiene la instancia real del usuario
    user = get_user_model().objects.get(username=request.user.username)
    
    # Filtrar productos alquilados por el usuario
    rented_products = RentalProduct.objects.filter(user=request.user.username)
    
    return render(request, 'rentals/rented_products.html', {'rented_products': rented_products})

