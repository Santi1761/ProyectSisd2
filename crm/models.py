from django.db import models

class Company(models.Model):
    nit = models.CharField(max_length=20, primary_key=True)
    name = models.CharField(max_length=100)
    industry = models.CharField(max_length=50, null=True, blank=True)
    address = models.CharField(max_length=255, null=True, blank=True)
    phone = models.CharField(max_length=20, null=True, blank=True)
    email = models.CharField(max_length=100, null=True, blank=True)
    country = models.CharField(max_length=50, null=True, blank=True)
    state = models.CharField(max_length=50, null=True, blank=True)
    creation_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name

class Contact(models.Model):
    contact_id = models.CharField(max_length=20, primary_key=True)
    company = models.ForeignKey(Company, related_name='contacts', on_delete=models.CASCADE)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    position = models.CharField(max_length=50, null=True, blank=True)
    phone = models.CharField(max_length=20, null=True, blank=True)
    email = models.CharField(max_length=100, null=True, blank=True)
    last_interaction_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class Department(models.Model):
    department_id = models.CharField(max_length=20, primary_key=True)
    department_name = models.CharField(max_length=50)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.department_name

class ContactDepartment(models.Model):
    contact = models.ForeignKey(Contact, on_delete=models.CASCADE)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    assignment_date = models.DateField(auto_now_add=True)

    class Meta:
        unique_together = ('contact', 'department')

class Interaction(models.Model):
    interaction_id = models.CharField(max_length=20, primary_key=True)
    contact = models.ForeignKey(Contact, related_name='interactions', on_delete=models.CASCADE)
    interaction_date = models.DateField(auto_now_add=True)
    interaction_type = models.CharField(max_length=50)
    notes = models.TextField(null=True, blank=True)

    def __str__(self):
        return f"Interaction {self.interaction_id} with {self.contact}"

class Opportunity(models.Model):
    opportunity_id = models.CharField(max_length=20, primary_key=True)
    company = models.ForeignKey(Company, related_name='opportunities', on_delete=models.CASCADE)
    contact = models.ForeignKey(Contact, related_name='opportunities', null=True, blank=True, on_delete=models.SET_NULL)
    opportunity_name = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)
    estimated_value = models.DecimalField(max_digits=15, decimal_places=2)
    creation_date = models.DateField(auto_now_add=True)
    estimated_close_date = models.DateField(null=True, blank=True)
    status = models.CharField(max_length=20, default='open')
    success_probability = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)

    def __str__(self):
        return self.opportunity_name

class OpportunityStage(models.Model):
    stage_id = models.CharField(max_length=20, primary_key=True)
    stage_name = models.CharField(max_length=50)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.stage_name

class OpportunityStageHistory(models.Model):
    opportunity = models.ForeignKey(Opportunity, on_delete=models.CASCADE)
    stage = models.ForeignKey(OpportunityStage, on_delete=models.CASCADE)
    change_date = models.DateField(auto_now_add=True)
    notes = models.TextField(null=True, blank=True)

    class Meta:
        unique_together = ('opportunity', 'stage')

class ProductService(models.Model):
    product_service_id = models.CharField(max_length=20, primary_key=True)
    product_service_name = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)
    price = models.DecimalField(max_digits=15, decimal_places=2)

    def __str__(self):
        return self.product_service_name

class OpportunityProductService(models.Model):
    opportunity = models.ForeignKey(Opportunity, on_delete=models.CASCADE)
    product_service = models.ForeignKey(ProductService, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    negotiated_price = models.DecimalField(max_digits=15, decimal_places=2)

    class Meta:
        unique_together = ('opportunity', 'product_service')

class Role(models.Model):
    role_id = models.CharField(max_length=20, primary_key=True)
    role_name = models.CharField(max_length=50)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.role_name

class UserAccount(models.Model):
    user_id = models.CharField(max_length=20, primary_key=True)
    company = models.ForeignKey(Company, related_name='user_accounts', on_delete=models.CASCADE)
    username = models.CharField(max_length=50, unique=True)
    password_hash = models.CharField(max_length=255)
    email = models.EmailField()
    created_at = models.DateTimeField(auto_now_add=True)
    last_login = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.username

class UserRole(models.Model):
    user = models.ForeignKey(UserAccount, on_delete=models.CASCADE)
    role = models.ForeignKey(Role, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('user', 'role')

class Contract(models.Model):
    contract_id = models.CharField(max_length=20, primary_key=True)
    company = models.ForeignKey(Company, related_name='contracts', on_delete=models.CASCADE)
    contract_number = models.CharField(max_length=50, unique=True)
    start_date = models.DateField()
    end_date = models.DateField()
    monthly_value = models.DecimalField(max_digits=15, decimal_places=2)

    def __str__(self):
        return self.contract_number

class DeliveryCertificate(models.Model):
    certificate_id = models.CharField(max_length=20, primary_key=True)
    contract = models.ForeignKey(Contract, related_name='delivery_certificates', on_delete=models.CASCADE)
    delivery_date = models.DateField()
    notes = models.TextField(null=True, blank=True)

    def __str__(self):
        return f"Certificate {self.certificate_id}"

class Category(models.Model):
    category_id = models.CharField(max_length=20, primary_key=True)
    category_name = models.CharField(max_length=50, unique=True)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.category_name

class Equipment(models.Model):
    equipment_id = models.CharField(max_length=20, primary_key=True)
    certificate = models.ForeignKey(DeliveryCertificate, related_name='equipments', on_delete=models.CASCADE)
    inventory_code = models.CharField(max_length=50, unique=True)
    description = models.CharField(max_length=255)
    active = models.BooleanField(default=True)
    category = models.ForeignKey(Category, null=True, blank=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.inventory_code
