from django.db import models

from users.models import User

class Employee(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    position = models.CharField(max_length=50)
    department = models.CharField(max_length=50)

    def __str__(self):
        return self.user.username
