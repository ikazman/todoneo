from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('create/', views.create, name='create'),
    path('current/', views.current, name='current'),
    path('completed/', views.completed, name='completed'),
    path('todo/<int:todo_pk>', views.view_tasks, name='tasks'),
    path('todo/<int:todo_pk>/complete', views.complete, name='complete'),
    path('todo/<int:todo_pk>/delete', views.delete, name='delete'),
]
