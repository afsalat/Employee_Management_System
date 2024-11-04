# urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('groups/', views.list_groups, name='group_list'),
    path('groups/create/', views.create_group, name='create_group'),
    path('groups/update/<int:group_id>/', views.update_group, name='update_group'),
    path('groups/delete/<int:group_id>/', views.delete_group, name='delete_group'),
]
