from django import forms
from django.forms import ModelForm

from .models import Todo

class DateInput(forms.DateInput):
    input_type = 'date'

class TodoForm(ModelForm):
    class Meta:
        model = Todo
        fields = ['title', 'memo', 'planed_date', 'important']
        widgets = {
            'planed_date': DateInput(),
        }
        labels = {'title': 'Заголовок',
                  'memo': 'Описание',
                  'planed_date': 'Дата выполнения',
                  'important': 'Важная задача'}
