from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name="menu"),
    path('tasks/', view_tasks, name='tasks'),
    path('templates/', Templates, name='templates'),
    path('projects/', Projects, name='projects'),
    path('complete/<int:pk>/', complete_task, name='complete')
]
