from django import forms
from django.forms import ModelForm

from .models import Project, Todo


class DateInput(forms.DateInput):
    input_type = 'date'


class TodoForm(ModelForm):
    class Meta:
        model = Todo
        fields = ['title', 'memo', 'planed_date', 'important', 'project']
        widgets = {
            'planed_date': DateInput(),
        }
        labels = {'title': 'Заголовок',
                  'project': 'Проект',
                  'memo': 'Описание',
                  'planed_date': 'Дата выполнения',
                  'important': 'Важная задача'}
