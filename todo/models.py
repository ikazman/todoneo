from datetime import date

from django.contrib.auth.models import User
from django.db import models


class Project(models.Model):
    """Модель проекта.
    Описание полей:
    1) название - текстовое поле с огарничением в 200 знаков,
    2) slug - url с проверкой допустимых символов, описание - текстовое поле.
    Название и url проверятся на уникальность.
    """

    title = models.CharField(max_length=200, unique=True,
                             verbose_name='Имя проекта')
    slug = models.SlugField(max_length=200, unique=True,
                            verbose_name='Идентификатор')
    description = models.TextField(blank=True, null=True,
                                   verbose_name='Описание')

    def __str__(self):
        return self.title  # возвращаем наименование при печати


class Todo(models.Model):
    title = models.CharField(max_length=100)
    memo = models.TextField(blank=True)
    created = models.DateTimeField(auto_now_add=True)
    planed_date = models.DateTimeField()
    date_completed = models.DateTimeField(null=True, blank=True)
    important = models.BooleanField(default=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    project = models.ForeignKey(Project, on_delete=models.SET_NULL,
                                related_name='project', blank=True, null=True,
                                verbose_name='Проект')

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['planed_date']
