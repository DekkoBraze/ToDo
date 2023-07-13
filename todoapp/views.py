from django.shortcuts import render
from django.views.generic import ListView
from django.http import HttpResponse
from .models import *

menu_lst = [{'title': "Задачи", 'url_name': 'tasks'},
        {'title': "Шаблоны", 'url_name': 'templates'},
        {'title': "Проекты", 'url_name': 'projects'},
]


def index(request):
    context = {'title': 'Меню', 'menu_lst': menu_lst}
    return render(request, 'todoapp/index.html', context=context)


class Tasks(ListView):
    model = Tasks
    template_name = 'todoapp/tasks.html'
    context_object_name = 'tasks_lst'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Меню задач'
        return context

def Templates(request):
    return HttpResponse('Teamplates')
def Projects(request):
    return HttpResponse('Projects')
#class Templates(ListView):
#    pass
#
#
#class Projects(ListView):
#    pass
