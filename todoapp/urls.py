from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name="menu"),
    path('tasks/', view_tasks, name='tasks'),
    path('templates/', Templates, name='templates'),
    path('projects/', Projects, name='projects'),
    path('complete/<int:pk>/', complete_task, name='complete'),
    path('add_task/', AddTask.as_view(), name='add_task'),
    path('<int:pk>/change_task/', ChangeTask.as_view(), name='change_task'),
    path('<int:pk>/delete_task/', DeleteTask.as_view(), name='delete_task')
]
