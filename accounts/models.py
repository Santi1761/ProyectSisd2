# accounts/models.py
from django.contrib.auth.models import AbstractUser 
from django.db import models

class Role(models.Model):
    role_id = models.CharField(max_length=20, primary_key=True)
    role_name = models.CharField(max_length=50, unique=True)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.role_name

class User(AbstractUser ):
    user_id = models.CharField(max_length=20, primary_key=True)
    nit = models.CharField(max_length=20, blank=True, null=True)  # Relación indirecta con Company
    email = models.EmailField(unique=True)
    roles = models.ManyToManyField(Role, related_name='users')

    # Especificar related_name para evitar conflictos
    groups = models.ManyToManyField(
        'auth.Group',
        related_name='custom_user_groups',  # Cambia esto a un nombre único
        blank=True,
        help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.',
        verbose_name='groups'
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='custom_user_permissions',  # Cambia esto a un nombre único
        blank=True,
        help_text='Specific permissions for this user.',
        verbose_name='user permissions'
    )

    def __str__(self):
        return self.username