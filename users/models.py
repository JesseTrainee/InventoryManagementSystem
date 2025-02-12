from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission
from core.base_models import BaseModel

class User(AbstractUser, BaseModel):
    ROLE_CHOICES = [
        ('admin', 'Administrador'),
        ('employee', 'Funcionário'),
    ]

    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default='employee')
    groups = models.ManyToManyField(Group, related_name="custom_user_group", blank=True)
    user_permissions = models.ManyToManyField(Permission, related_name="custom_user_permissions", blank=True)

    def __str__(self):
        return self.username