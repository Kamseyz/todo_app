from django.urls import path
from . import views

urlpatterns = [
    path('task/', views.task, name='task'),
    path('task_edit/<int:pk>/', views.task_edit, name='task_edit'),
    path('task_add/', views.task_add, name='task_add'),
    path('task_delete/<int:pk>/', views.task_delete, name='task_delete'),
]
