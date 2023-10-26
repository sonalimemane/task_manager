from django import forms
from .models import Task
from django.contrib.auth.models import User


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'description', 'project', 'assigned_to', 'due_date', 'status']
        widgets = {
            'due_date': forms.TextInput(attrs={'type': 'date'}),
        }