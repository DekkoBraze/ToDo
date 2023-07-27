from .models import *


class DataMixin:
    menu_lst = [{'title': "Задачи", 'url_name': 'tasks', 'page_type': 1},
                {'title': "Шаблоны", 'url_name': 'templates', 'page_type': 2},
                {'title': "Проекты", 'url_name': 'projects', 'page_type': 3},
                ]

    def get_user_context(self, **kwargs):
        context = kwargs
        context['menu_lst'] = self.menu_lst
        #context['page_type'] = 0
        return context
