from django import forms
from .models import Todo


class TodoForm(forms.ModelForm):

  class Meta:
    model = Todo
    fields = ['title', 'details']
    widgets = {
        'title': forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Enter task title...',
            }
        ),
        'details': forms.Textarea(
            attrs={
                'class': 'form-control',
                'rows': 3,
                'placeholder': 'Enter task details...',
            }
        ),
    }