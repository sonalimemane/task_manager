from django.urls import path
from . import views

urlpatterns = [
    # Task management views
    path('', views.task_list, name='task_list'),
    path('create/', views.create_task, name='create_task'),
    path('task_detail/<int:task_id>/', views.task_detail, name='task_detail'),
    path('edit_task/<int:task_id>/edit/', views.edit_task, name='edit_task'),
    path('delete_tasks/<int:task_id>/delete/', views.delete_task, name='delete_task'),
    path('project_list', views.project_list, name='project_list'),
    path('project_detail', views.project_detail, name='project_detail'),

]