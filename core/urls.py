from django.contrib import admin
from django.urls import path
from task.views import task_create, task_delete, task_list, task_update

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', task_list, name='task_list'),
    path('update/<int:pk>/', task_update, name='task_update'),
    path('create/', task_create, name='task_create'),
    path('delete/<int:pk>/', task_delete, name='task_delete'),
]
