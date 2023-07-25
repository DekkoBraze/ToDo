from .models import *

menu_lst = [{'title': "Задачи", 'url_name': 'tasks', 'page_type': 1},
        {'title': "Шаблоны", 'url_name': 'templates', 'page_type': 2},
        {'title': "Проекты", 'url_name': 'projects', 'page_type': 3},
]


class TaskFormMixin:
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Менеджер задач'
        context['menu_lst'] = menu_lst
        context['page_type'] = 0
        return context
