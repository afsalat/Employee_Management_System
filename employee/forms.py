from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Employee


class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = ['user', 'position', 'department', 'email', 'phone', 'salary']
