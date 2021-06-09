from django.contrib import admin

from .models import Todo


class TodoAdmin(admin.ModelAdmin):
    list_display = ('pk', 'memo', 'created', 'date_completed', 'important', 'user')
    search_fields = ('user',)
    list_filter = ('created',)
    empty_value_display = '-пусто-'


admin.site.register(Todo, TodoAdmin)
