from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth.decorators import permission_required, login_required
from django.contrib import messages
from .models import Employee
from .forms import EmployeeForm

@login_required()
@permission_required('employees.add_employee', raise_exception=True)
def add_employee(request):
    if request.method == "POST":
        form = EmployeeForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Employee added successfully.")
            return redirect('employee_create')
        else:
            messages.error(request, "There was an error adding the employee.")
    else:
        form = EmployeeForm()
    
    return render(request, 'employee/employee_create.html', {'form': form})



@login_required()
# @permission_required('employees.employee_list', raise_exception=True)
def view_employees(request):
    employees = Employee.objects.all()
    return render(request, 'employee/employee_list.html', {'employees':employees})



@login_required()
@permission_required('employees.delete_employee', raise_exception=True)
def remove_employee(request, employee_id):
    employee = Employee.objects.filter(id=employee_id).first()
    if request.method == "POST":
        employee.delete()
        return redirect('employee_list')   
    return render(request, 'employee/employee_confirm_delete.html', {'employee':employee})



@login_required()
@permission_required('employees.change_employee', raise_exception=True)
def update_employee(request, employee_id):
    employee = get_object_or_404(Employee, id=employee_id)
    if request.method == "POST":
        form = EmployeeForm(request.POST, instance=employee)
        if form.is_valid():
            form.save()
            return redirect('employee_list')  # Redirect to the employee list page
    else:
        form = EmployeeForm(instance=employee)
    return render(request, 'employee/employee_create.html', {'form': form, 'employee': employee})