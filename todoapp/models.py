from django.db import models


class Tasks(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField(blank=True)
    project = models.ForeignKey("Projects", on_delete=models.PROTECT)
    time_create = models.DateTimeField(auto_now_add=True)
    time_complete = models.DateTimeField(null=True)


class Projects(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField(blank=True)
    progress = models.IntegerField()
    time_create = models.DateTimeField(auto_now_add=True)
    time_complete = models.DateTimeField(null=True)
