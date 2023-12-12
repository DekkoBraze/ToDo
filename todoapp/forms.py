from django import forms
from .models import *
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm


class TaskForm(forms.ModelForm):
    def __init__(self, user=None, **kwargs):
        self.username = kwargs.pop('username')
        super(TaskForm, self).__init__(**kwargs)
        self.fields['project'].queryset = Projects.objects.filter(time_complete=None, user=self.username)

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


class TemplateForm(forms.ModelForm):
    def __init__(self, user=None, **kwargs):
        self.username = kwargs.pop('username')
        super(TemplateForm, self).__init__(**kwargs)
        self.fields['project'].queryset = Projects.objects.filter(time_complete=None, user=self.username)

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
        else:
            return self.cleaned_data['title']


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


class RegisterUserForm(UserCreationForm):
    username = forms.CharField(label='Логин', widget=forms.TextInput(attrs={'class': 'form-input'}))
    email = forms.EmailField(label='Email', widget=forms.EmailInput(attrs={'class': 'form-input'}))
    password1 = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': 'form-input'}))
    password2 = forms.CharField(label='Повтор пароля', widget=forms.PasswordInput(attrs={'class': 'form-input'}))

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')


class LoginUserForm(AuthenticationForm):
    username = forms.CharField(label='Логин', widget=forms.TextInput(attrs={'class': 'form-input'}))
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': 'form-input'}))