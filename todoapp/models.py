from django.db import models
from django.shortcuts import reverse


class Tasks(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField(blank=True)
    project = models.ForeignKey("Projects", on_delete=models.PROTECT, null=True, blank=True)
    time_create = models.DateTimeField(auto_now_add=True)
    time_complete = models.DateTimeField(null=True, blank=True)


class Projects(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField(blank=True)
    progress = models.IntegerField()
    time_create = models.DateTimeField(auto_now_add=True)
    time_complete = models.DateTimeField(null=True, blank=True)
