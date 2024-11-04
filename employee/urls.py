from django.urls import path
from . import views


urlpatterns = [
    path('add/', views.add_employee, name='employee_create'),
    path('employee_list/', views.view_employees, name='employee_list'),
    path('delete_employee/<int:employee_id>', views.remove_employee, name='employee_delete'),
    path('update_employeee/<int:employee_id>/', views.update_employee, name='employee_update'),
]