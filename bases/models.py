from django.db import models

# Modelo Company
class Company(models.Model):
    nit = models.CharField(max_length=20, primary_key=True)
    name = models.CharField(max_length=100)
    industry = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    phone = models.CharField(max_length=50)
    email = models.EmailField(max_length=100)
    country = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    creation_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

# Modelo Contact
class Contact(models.Model):
    contact_id = models.CharField(max_length=20, primary_key=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone = models.CharField(max_length=20)
    email = models.EmailField(max_length=100)
    notes = models.TextField(null=True, blank=True)
    last_interaction_date = models.DateField(null=True, blank=True)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

# Modelo Contract
class Contract(models.Model):
    contract_id = models.CharField(max_length=20, primary_key=True)
    contact = models.ForeignKey(Contact, on_delete=models.CASCADE)
    contract_number = models.CharField(max_length=50, unique=True)
    start_date = models.DateField()
    end_date = models.DateField()
    monthly_value = models.DecimalField(max_digits=15, decimal_places=2)

    def __str__(self):
        return self.contract_number

# Modelo Opportunity
class Opportunity(models.Model):
    opportunity_id = models.CharField(max_length=20, primary_key=True)
    contact = models.ForeignKey(Contact, on_delete=models.CASCADE)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    opportunity_name = models.CharField(max_length=100)
    description = models.TextField()
    estimated_value = models.DecimalField(max_digits=15, decimal_places=2)
    estimated_close_date = models.DateField()
    status = models.CharField(max_length=20)
    success_probability = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return self.opportunity_name

# Modelo Opportunity Stage
class OpportunityStage(models.Model):
    stage_id = models.CharField(max_length=20, primary_key=True)
    stage_name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.stage_name

# Modelo Opportunity Stage History
class OpportunityStageHistory(models.Model):
    opportunity = models.ForeignKey(Opportunity, on_delete=models.CASCADE)
    stage = models.ForeignKey(OpportunityStage, on_delete=models.CASCADE)
    change_date = models.DateField()
    notes = models.TextField(null=True, blank=True)

    def __str__(self):
        return f"{self.opportunity} - {self.stage}"

# Modelo Product Service
class ProductService(models.Model):
    product_service_id = models.CharField(max_length=20, primary_key=True)
    product_service_name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=15, decimal_places=2)

    def __str__(self):
        return self.product_service_name

# Modelo Opportunity Product Service
class OpportunityProductService(models.Model):
    opportunity = models.ForeignKey(Opportunity, on_delete=models.CASCADE)
    product_service = models.ForeignKey(ProductService, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    negotiated_price = models.DecimalField(max_digits=15, decimal_places=2)

    def __str__(self):
        return f"{self.opportunity} - {self.product_service}"

# Modelo User Role
class Role(models.Model):
    role_id = models.CharField(max_length=20, primary_key=True)
    role_name = models.CharField(max_length=50)
    description = models.TextField()

    def __str__(self):
        return self.role_name

class UserAccount(models.Model):
    user_id = models.CharField(max_length=20, primary_key=True)
    nit = models.ForeignKey(Company, on_delete=models.CASCADE)
    username = models.CharField(max_length=50, unique=True)
    password = models.CharField(max_length=255)
    email = models.EmailField()
    enabled = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    last_login = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.username

class UserRole(models.Model):
    user = models.ForeignKey(UserAccount, on_delete=models.CASCADE)
    role = models.ForeignKey(Role, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user} - {self.role}"

# Modelo Equipment
class Equipment(models.Model):
    equipment_id = models.CharField(max_length=20, primary_key=True)
    inventory_code = models.CharField(max_length=50, unique=True)
    description = models.TextField()
    active = models.BooleanField(default=True)
    acquisition_date = models.DateField()

    def __str__(self):
        return self.inventory_code

# Modelo Category
class Category(models.Model):
    category_id = models.CharField(max_length=20, primary_key=True)
    category_name = models.CharField(max_length=50)

    def __str__(self):
        return self.category_name

# Modelo Delivery Certificate
class DeliveryCertificate(models.Model):
    certificate_id = models.CharField(max_length=20, primary_key=True)
    contract = models.ForeignKey(Contract, on_delete=models.CASCADE)
    delivery_date = models.DateField()
    notes = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.certificate_id
