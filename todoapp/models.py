from django.db import models
from django.shortcuts import reverse


class Tasks(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField(blank=True)
    project = models.ForeignKey("Projects", on_delete=models.CASCADE, null=True, blank=True)
    time_create = models.DateTimeField(auto_now_add=True)
    time_complete = models.DateTimeField(null=True, blank=True)
    user = models.CharField(max_length=50, blank=True, default='')


class TaskTemplate(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField(blank=True)
    project = models.ForeignKey("Projects", on_delete=models.CASCADE, null=True, blank=True)
    user = models.CharField(max_length=50, blank=True, default='')


class Projects(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField(blank=True)
    progress = models.IntegerField(default=0)
    time_create = models.DateTimeField(auto_now_add=True)
    time_complete = models.DateTimeField(null=True, blank=True)
    user = models.CharField(max_length=50, blank=True, default='')

    def __str__(self):
        return self.title

    def add_progress(self):
        self.progress += 1
        self.save()
