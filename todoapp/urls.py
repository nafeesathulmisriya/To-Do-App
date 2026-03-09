from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('create/', views.create_task, name='create_task'),

    # ✅ correct task details route
    path('tasks/', views.task_details, name='task_details'),


    path('task/toggle/<int:task_id>/', views.toggle_task, name='toggle_task'),
    path('task/delete/<int:task_id>/', views.delete_task, name='delete_task'),
    path('task/edit/<int:task_id>/', views.edit_task, name='edit_task'),
    
    path('task/complete/<int:task_id>/', views.mark_completed, name='mark_completed'),
    path('tasks/completed/', views.completed_tasks, name='completed_tasks'),


   
]


