from django.db import models
from django.contrib.auth.models import User

class Project(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()

class Task(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    assigned_to = models.ManyToManyField(User, related_name='tasks_assigned', blank=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='tasks_created')
    created_at = models.DateTimeField(auto_now_add=True)
    due_date = models.DateTimeField()
    status = models.CharField(max_length=20, choices=[('Todo', 'Todo'), ('In Progress', 'In Progress'), ('Done', 'Done')])
