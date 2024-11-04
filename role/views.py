# views.py
from django.contrib.auth.models import Group, Permission
from django.shortcuts import get_object_or_404, render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required, permission_required


@login_required
@permission_required('group.view_group', raise_exception=True)
def list_groups(request):
    groups = Group.objects.all()
    return render(request, 'role/list_role.html', {'groups': groups})



@login_required
@permission_required('group.add_group', raise_exception=True)
def create_group(request):
    permissions = Permission.objects.all()

    if request.method == 'POST':
        group_name = request.POST.get('name')
        selected_permissions = request.POST.getlist('permissions')

        group = Group.objects.create(name=group_name)

        for perm_id in selected_permissions:
            permission = get_object_or_404(Permission, id=perm_id)
            group.permissions.add(permission)

        messages.success(request, f'Group "{group_name}" created successfully with selected permissions.')
        return redirect('group_list')

    return render(request, 'role/create_role.html', {'permissions': permissions})





@login_required
@permission_required('group.update_group', raise_exception=True)
def update_group(request, group_id):
    group = get_object_or_404(Group, id=group_id)

    if request.method == 'POST':
        group_name = request.POST.get('name')
        permission_ids = request.POST.getlist('permissions')

        if group_name:
            group.name = group_name
            group.save()

        group.permissions.clear()
        for perm_id in permission_ids:
            permission = Permission.objects.get(id=perm_id)
            group.permissions.add(permission)

        return redirect('group_list') 

    permissions = Permission.objects.all()
    return render(request, 'role/update_role.html', {'group': group, 'permissions': permissions, 'group_permissions': group.permissions.all()})





@login_required
@permission_required('group.delete_group', raise_exception=True)
def delete_group(request, group_id):
    group = get_object_or_404(Group, id=group_id)

    if request.method == 'POST':
        group.delete()
        return redirect('group_list')

    return render(request, 'role/conform_delete_role.html', {'group': group})
