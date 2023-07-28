from django import forms
from .models import *


class TaskForm(forms.ModelForm):
    class Meta:
        model = Tasks
        fields = ['title', 'content', 'project']
        labels = {
            'title': 'Задача',
            'content': 'Описание',
            'project': 'Проект',
        }
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-input'}),
            'content': forms.Textarea(attrs={'cols': 50, 'rows': 3}),
        }

    def __init__(self, user=None, **kwargs):
        super(TaskForm, self).__init__(**kwargs)
        self.fields['project'].queryset = Projects.objects.filter(time_complete=None)


class TemplateForm(forms.ModelForm):
    class Meta:
        model = TaskTemplate
        fields = ['title', 'content', 'project']
        labels = {
            'title': 'Задача',
            'content': 'Описание',
            'project': 'Проект',
        }
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-input'}),
            'content': forms.Textarea(attrs={'cols': 50, 'rows': 3}),
        }

    def clean_title(self):
        title = self.cleaned_data['title']
        dublicates = TaskTemplate.objects.filter(title=title)

        if dublicates.exists():
            raise ValueError('Шаблон с таким именем уже существует. Вы точно не ошиблись?')


class ProjectForm(forms.ModelForm):
    class Meta:
        model = Projects
        fields = ['title', 'content']
        labels = {
            'title': 'Название проекта',
            'content': 'Описание',
        }
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-input'}),
            'content': forms.Textarea(attrs={'cols': 50, 'rows': 3}),
        }
