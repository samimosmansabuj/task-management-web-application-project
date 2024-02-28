from django import forms
from .models import Task

class Task_Form(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'description', 'due_date', 'priority']
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-control', 'placeholder': 'Enter Task Title'
            }),
            'description': forms.Textarea(attrs={
                'class': 'form-control'
            }),
            'due_date': forms.DateTimeInput(attrs={
                'class': 'form-control', 'type': 'datetime-local'
            }),
            'priority': forms.Select(attrs={
                'class': 'form-control'
            }),
        }

