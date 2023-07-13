from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name="menu"),
    path('tasks/', Tasks.as_view(), name='tasks'),
    path('templates/', Templates, name='templates'),
    path('projects/', Projects, name='projects')
]
