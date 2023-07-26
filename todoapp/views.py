import time
from datetime import datetime
from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, FormView
from django.http import HttpResponse
from .models import *
from django.shortcuts import redirect
from django.db.models import F, Func, Value, CharField
from .forms import *
from django.urls import reverse_lazy
from .utils import *


def index(request):
    context = {'title': 'Меню', 'menu_lst': DataMixin.menu_lst}
    return render(request, 'todoapp/index.html', context=context)


def view_tasks(request):
    uncompleted_tasks = Tasks.objects.filter(time_complete=None).order_by('-time_create')
    completed_tasks = Tasks.objects.exclude(time_complete=None).order_by('-time_complete')

    context = {'title': 'Задачи', 'menu_lst': DataMixin.menu_lst, 'page_type': 1, 'uncompleted_tasks': uncompleted_tasks,
               'completed_tasks': completed_tasks}

    return render(request, 'todoapp/tasks.html', context=context)


def view_projects(request):
    uncompleted_projects = Projects.objects.filter(time_complete=None).order_by('-time_create')
    completed_projects = Projects.objects.exclude(time_complete=None).order_by('-time_complete')

    context = {'title': 'Проекты', 'menu_lst': DataMixin.menu_lst, 'page_type': 3, 'uncompleted_projects': uncompleted_projects,
               'completed_projects': completed_projects}

    return render(request, 'todoapp/projects.html', context=context)


def complete_task(request, pk):
    task = Tasks.objects.get(pk=pk)
    task.project.add_progress()
    task.time_complete = datetime.now()
    task.save()

    return redirect('tasks')


def add_project_task(request, pk):
    project = Projects.objects.get(pk=pk)
    t = Tasks(title='Задача по проекту', project=project)
    t.save()

    return redirect('tasks')


class AddTask(DataMixin, CreateView):
    form_class = TaskForm
    template_name = 'todoapp/add_content.html'
    success_url = reverse_lazy('tasks')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Добавление задачи")
        context = dict(list(context.items()) + list(c_def.items()))
        return context


class ChangeTask(DataMixin, UpdateView):
    form_class = TaskForm
    model = Tasks
    template_name = 'todoapp/change_content.html'
    success_url = reverse_lazy('tasks')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Изменение задачи")
        context = dict(list(context.items()) + list(c_def.items()))
        return context


class DeleteTask(DataMixin, DeleteView):
    model = Tasks
    template_name = 'todoapp/delete_content.html'
    success_url = reverse_lazy('tasks')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Удаление задачи", text='Вы уверены, что хотите удалить задачу?', action='Удалить!')
        context = dict(list(context.items()) + list(c_def.items()))
        return context


class AddProject(DataMixin, CreateView):
    form_class = ProjectForm
    template_name = 'todoapp/add_content.html'
    success_url = reverse_lazy('projects')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Добавление проекта")
        context = dict(list(context.items()) + list(c_def.items()))
        return context


class ChangeProject(DataMixin, UpdateView):
    form_class = ProjectForm
    model = Projects
    template_name = 'todoapp/change_content.html'
    success_url = reverse_lazy('projects')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Изменение проекта")
        context = dict(list(context.items()) + list(c_def.items()))
        return context


class DeleteProject(DataMixin, DeleteView):
    model = Projects
    template_name = 'todoapp/delete_content.html'
    success_url = reverse_lazy('projects')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Удаление проекта",
                                      text='Вы уверены, что хотите удалить проект? Все задачи, связанные с ним, будут также удалены!',
                                      action='Удалить!')
        context = dict(list(context.items()) + list(c_def.items()))
        return context


class CompleteProject(DataMixin, UpdateView):
    model = Projects
    template_name = 'todoapp/delete_content.html'
    success_url = reverse_lazy('projects')
    fields = ("time_complete", )

    def form_valid(self, form):
        project = form.instance
        tasks = project.tasks_set.all()
        tasks.delete()
        project.time_complete = datetime.now()
        project.save()

        return super().form_valid(form)

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Завершение проекта",
                                      text='Вы уверены, что хотите завершить проект? Все задачи, связанные с ним, будут удалены!',
                                      action='Завершить!')
        context = dict(list(context.items()) + list(c_def.items()))
        return context


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
#class Templates(ListView):
#    pass
#
#
#class Projects(ListView):
#    pass
