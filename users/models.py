from django.contrib.auth.models import AbstractUser, Group
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver

class User(AbstractUser):
    ROLE_CHOICES = (
        ('admin', 'Admin'),
        ('employee', 'Employee'),
    )
    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default='employee')

    def assign_group_based_on_role(self):
        self.groups.clear()

        if self.role == 'admin':
            admin_group, created = Group.objects.get_or_create(name='Admin')
            self.groups.add(admin_group)
        elif self.role == 'employee':
            employee_group, created = Group.objects.get_or_create(name='Employee')
            self.groups.add(employee_group)

        self.save()

