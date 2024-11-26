# Generated by Django 3.1.12 on 2024-11-26 02:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('category_id', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('category_name', models.CharField(max_length=50, unique=True)),
                ('description', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Company',
            fields=[
                ('nit', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('industry', models.CharField(blank=True, max_length=50, null=True)),
                ('address', models.CharField(blank=True, max_length=255, null=True)),
                ('phone', models.CharField(blank=True, max_length=20, null=True)),
                ('email', models.CharField(blank=True, max_length=100, null=True)),
                ('country', models.CharField(blank=True, max_length=50, null=True)),
                ('state', models.CharField(blank=True, max_length=50, null=True)),
                ('creation_date', models.DateField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('contact_id', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('position', models.CharField(blank=True, max_length=50, null=True)),
                ('phone', models.CharField(blank=True, max_length=20, null=True)),
                ('email', models.CharField(blank=True, max_length=100, null=True)),
                ('last_interaction_date', models.DateField(blank=True, null=True)),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='contacts', to='crm.company')),
            ],
        ),
        migrations.CreateModel(
            name='Contract',
            fields=[
                ('contract_id', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('contract_number', models.CharField(max_length=50, unique=True)),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('monthly_value', models.DecimalField(decimal_places=2, max_digits=15)),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='contracts', to='crm.company')),
            ],
        ),
        migrations.CreateModel(
            name='DeliveryCertificate',
            fields=[
                ('certificate_id', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('delivery_date', models.DateField()),
                ('notes', models.TextField(blank=True, null=True)),
                ('contract', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='delivery_certificates', to='crm.contract')),
            ],
        ),
        migrations.CreateModel(
            name='Department',
            fields=[
                ('department_id', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('department_name', models.CharField(max_length=50)),
                ('description', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Opportunity',
            fields=[
                ('opportunity_id', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('opportunity_name', models.CharField(max_length=100)),
                ('description', models.TextField(blank=True, null=True)),
                ('estimated_value', models.DecimalField(decimal_places=2, max_digits=15)),
                ('creation_date', models.DateField(auto_now_add=True)),
                ('estimated_close_date', models.DateField(blank=True, null=True)),
                ('status', models.CharField(default='open', max_length=20)),
                ('success_probability', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True)),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='opportunities', to='crm.company')),
                ('contact', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='opportunities', to='crm.contact')),
            ],
        ),
        migrations.CreateModel(
            name='OpportunityStage',
            fields=[
                ('stage_id', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('stage_name', models.CharField(max_length=50)),
                ('description', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='ProductService',
            fields=[
                ('product_service_id', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('product_service_name', models.CharField(max_length=100)),
                ('description', models.TextField(blank=True, null=True)),
                ('price', models.DecimalField(decimal_places=2, max_digits=15)),
            ],
        ),
        migrations.CreateModel(
            name='Role',
            fields=[
                ('role_id', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('role_name', models.CharField(max_length=50)),
                ('description', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='UserAccount',
            fields=[
                ('user_id', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('username', models.CharField(max_length=50, unique=True)),
                ('password_hash', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=254)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('last_login', models.DateTimeField(blank=True, null=True)),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_accounts', to='crm.company')),
            ],
        ),
        migrations.CreateModel(
            name='Interaction',
            fields=[
                ('interaction_id', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('interaction_date', models.DateField(auto_now_add=True)),
                ('interaction_type', models.CharField(max_length=50)),
                ('notes', models.TextField(blank=True, null=True)),
                ('contact', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='interactions', to='crm.contact')),
            ],
        ),
        migrations.CreateModel(
            name='Equipment',
            fields=[
                ('equipment_id', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('inventory_code', models.CharField(max_length=50, unique=True)),
                ('description', models.CharField(max_length=255)),
                ('active', models.BooleanField(default=True)),
                ('category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='crm.category')),
                ('certificate', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='equipments', to='crm.deliverycertificate')),
            ],
        ),
        migrations.CreateModel(
            name='UserRole',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('role', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='crm.role')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='crm.useraccount')),
            ],
            options={
                'unique_together': {('user', 'role')},
            },
        ),
        migrations.CreateModel(
            name='OpportunityStageHistory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('change_date', models.DateField(auto_now_add=True)),
                ('notes', models.TextField(blank=True, null=True)),
                ('opportunity', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='crm.opportunity')),
                ('stage', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='crm.opportunitystage')),
            ],
            options={
                'unique_together': {('opportunity', 'stage')},
            },
        ),
        migrations.CreateModel(
            name='OpportunityProductService',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField(default=1)),
                ('negotiated_price', models.DecimalField(decimal_places=2, max_digits=15)),
                ('opportunity', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='crm.opportunity')),
                ('product_service', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='crm.productservice')),
            ],
            options={
                'unique_together': {('opportunity', 'product_service')},
            },
        ),
        migrations.CreateModel(
            name='ContactDepartment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('assignment_date', models.DateField(auto_now_add=True)),
                ('contact', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='crm.contact')),
                ('department', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='crm.department')),
            ],
            options={
                'unique_together': {('contact', 'department')},
            },
        ),
    ]
