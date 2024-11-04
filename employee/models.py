from django.contrib.auth.models import Group
from django.db import models
from django.conf import settings

class Employee(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    position = models.ForeignKey(Group, on_delete=models.CASCADE)
    department = models.CharField(max_length=100)
    hire_date = models.DateField(auto_now_add=True)
    email = models.EmailField(null=True)
    phone = models.IntegerField(null=True)
    salary = models.IntegerField(null=True)

    class Meta:
        permissions = [
            ("can_view_salary", "Can view employee salary"),
            ("can_edit_position", "Can edit employee position"),
        ]

    def __str__(self):
        return self.user.username
