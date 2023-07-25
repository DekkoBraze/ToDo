import time
from datetime import datetime
from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.http import HttpResponse
from .models import *
from django.shortcuts import redirect
from django.db.models import F, Func, Value, CharField
from .forms import *
from django.urls import reverse_lazy
from .utils import *

menu_lst = [{'title': "Задачи", 'url_name': 'tasks', 'page_type': 1},
        {'title': "Шаблоны", 'url_name': 'templates', 'page_type': 2},
        {'title': "Проекты", 'url_name': 'projects', 'page_type': 3},
]


def index(request):
    context = {'title': 'Меню', 'menu_lst': menu_lst}
    return render(request, 'todoapp/index.html', context=context)


def complete_task(request, pk):
    task = Tasks.objects.get(pk=pk)
    task.time_complete = datetime.now()
    task.save()

    return redirect('tasks')
    #return HttpResponse(task.time_complete)


def view_tasks(request):
    uncompleted_tasks = Tasks.objects.filter(time_complete=None).order_by('-time_create')
    completed_tasks = Tasks.objects.exclude(time_complete=None).order_by('-time_complete')

    context = {'title': 'Задачи', 'menu_lst': menu_lst, 'page_type': 1, 'uncompleted_tasks': uncompleted_tasks,
               'completed_tasks': completed_tasks}

    return render(request, 'todoapp/tasks.html', context=context)


class AddTask(TaskFormMixin, CreateView):
    form_class = TaskForm
    template_name = 'todoapp/add_task.html'
    success_url = reverse_lazy('tasks')


class ChangeTask(TaskFormMixin, UpdateView):
    form_class = TaskForm
    model = Tasks
    template_name = 'todoapp/change_task.html'
    success_url = reverse_lazy('tasks')


class DeleteTask(TaskFormMixin, DeleteView):
    model = Tasks
    template_name = 'todoapp/delete_task.html'
    success_url = reverse_lazy('tasks')


#class ViewTasks(ListView):
#    model = Tasks
#    template_name = 'todoapp/tasks.html'
#    context_object_name = 'tasks_lst'
#
#    def get_queryset(self):
#        return Tasks.objects.order_by('-time_complete', '-time_create')
#
#    def get_context_data(self, *, object_list=None, **kwargs):
#        context = super().get_context_data(**kwargs)
#        context['title'] = 'Задачи'
#        context['menu_lst'] = menu_lst
#        context['page_type'] = 1
#        return context

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
