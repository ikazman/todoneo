from django.contrib import admin

from .models import Project, Todo


class TodoAdmin(admin.ModelAdmin):
    list_display = ('pk', 'title', 'project', 'memo', 'created', 'date_completed', 'important', 'user')
    search_fields = ('user',)
    list_filter = ('created',)
    empty_value_display = '-пусто-'


class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'slug')
    search_fields = ('description',)  # поиск по описанию логичней
    list_filter = ('title',)
    prepopulated_fields = {'slug': ('title',)}
    empty_value_display = '-пусто-'


admin.site.register(Todo, TodoAdmin)
admin.site.register(Project, ProjectAdmin)
