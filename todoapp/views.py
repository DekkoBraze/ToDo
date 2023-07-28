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


class TemplateView(DataMixin, ListView):
    model = TaskTemplate
    template_name = 'todoapp/templates.html'
    context_object_name = 'templates'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(page_type=2, title='Шаблоны')
        context = dict(list(context.items()) + list(c_def.items()))
        return context


def view_projects(request):
    uncompleted_projects = Projects.objects.filter(time_complete=None).order_by('-time_create')
    completed_projects = Projects.objects.exclude(time_complete=None).order_by('-time_complete')

    context = {'title': 'Проекты', 'menu_lst': DataMixin.menu_lst, 'page_type': 3, 'uncompleted_projects': uncompleted_projects,
               'completed_projects': completed_projects}

    return render(request, 'todoapp/projects.html', context=context)


def complete_task(request, pk):
    task = Tasks.objects.get(pk=pk)
    if (task.project):
        task.project.add_progress()
    task.time_complete = datetime.now()
    task.save()

    return redirect('tasks')


def add_project_task(request, pk):
    project = Projects.objects.get(pk=pk)
    t = Tasks(title='Задача по проекту', project=project)
    t.save()

    return redirect('tasks')


def create_template(request, pk):
    task = Tasks.objects.get(pk=pk)
    dublicates = TaskTemplate.objects.filter(title=task.title)

    if dublicates.exists():
        raise ValueError('Шаблон с таким именем уже существует. Вы точно не ошиблись?')
    else:
        template = TaskTemplate(title=task.title, content=task.content, project=task.project)
        template.save()

    return redirect('tasks')


def create_task_from_template(request, pk):
    template = TaskTemplate.objects.get(pk=pk)
    task = Tasks(title=template.title, content=template.content, project=template.project)
    task.save()

    return redirect('templates')


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


class AddTemplate(DataMixin, CreateView):
    form_class = TemplateForm
    template_name = 'todoapp/add_content.html'
    success_url = reverse_lazy('templates')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Добавление шаблона")
        context = dict(list(context.items()) + list(c_def.items()))
        return context


class ChangeTemplate(DataMixin, UpdateView):
    form_class = TemplateForm
    model = TaskTemplate
    template_name = 'todoapp/change_content.html'
    success_url = reverse_lazy('templates')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Изменение шаблона")
        context = dict(list(context.items()) + list(c_def.items()))
        return context


class DeleteTemplate(DataMixin, DeleteView):
    model = TaskTemplate
    template_name = 'todoapp/delete_content.html'
    success_url = reverse_lazy('templates')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Удаление шаблона", text='Вы уверены, что хотите удалить шаблон?', action='Удалить!')
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
