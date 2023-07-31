from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name="menu"),
    path('tasks/', view_tasks, name='tasks'),
    path('templates/', view_templates, name='templates'),
    path('projects/', view_projects, name='projects'),
    path('<int:pk>/complete_task/', complete_task, name='complete_task'),
    path('add_task/', AddTask.as_view(), name='add_task'),
    path('<int:pk>/change_task/', ChangeTask.as_view(), name='change_task'),
    path('<int:pk>/delete_task/', DeleteTask.as_view(), name='delete_task'),
    path('add_project/', AddProject.as_view(), name='add_project'),
    path('<int:pk>/change_project/', ChangeProject.as_view(), name='change_project'),
    path('<int:pk>/delete_project/', DeleteProject.as_view(), name='delete_project'),
    path('<int:pk>/add_project_task/', add_project_task, name='add_project_task'),
    path('<int:pk>/complete_project/', CompleteProject.as_view(), name='complete_project'),
    path('<int:pk>/create_template/', create_template, name='create_template'),
    path('<int:pk>/use_template/', create_task_from_template, name='use_template'),
    path('add_template/', AddTemplate.as_view(), name='add_template'),
    path('<int:pk>/change_template/', ChangeTemplate.as_view(), name='change_template'),
    path('<int:pk>/delete_template/', DeleteTemplate.as_view(), name='delete_template'),
    path('register/', RegisterUser.as_view(), name='register'),
    path('login/', LoginUser.as_view(), name='login'),
    path('logout/', logout_user, name='logout')
]
