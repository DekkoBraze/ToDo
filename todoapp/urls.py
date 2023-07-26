from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name="menu"),
    path('tasks/', view_tasks, name='tasks'),
    path('templates/', Templates, name='templates'),
    path('projects/', view_projects, name='projects'),
    path('<int:pk>/complete_task/', complete_task, name='complete_task'),
    path('add_task/', AddTask.as_view(), name='add_task'),
    path('<int:pk>/change_task/', ChangeTask.as_view(), name='change_task'),
    path('<int:pk>/delete_task/', DeleteTask.as_view(), name='delete_task'),
    path('add_project/', AddProject.as_view(), name='add_project'),
    path('<int:pk>/change_project/', ChangeProject.as_view(), name='change_project'),
    path('<int:pk>/delete_project/', DeleteProject.as_view(), name='delete_project'),
    path('<int:pk>/add_project_task/', add_project_task, name='add_project_task'),
    path('<int:pk>/complete_project/', CompleteProject.as_view(), name='complete_project')
]
