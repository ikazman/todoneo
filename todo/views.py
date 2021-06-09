from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render
from django.utils import timezone

from .forms import TodoForm
from .models import Todo


def index(request):
    """View-функция для рендеринга главной страницы."""
    return render(request, 'index.html')


@login_required
def create(request):
    if request.method == 'POST':
        form = TodoForm(request.POST or None, files=request.FILES or None)
        if form.is_valid():
            new_task = form.save(commit=False)
            new_task.user = request.user
            new_task.save()
            return redirect('current')

        return render(request, 'create.html', {'form': form})

    form = TodoForm()
    return render(request, 'create.html', {'form': form})


@login_required
def edit_task(request, todo_pk):
    task = get_object_or_404(Todo, pk=todo_pk, user=request.user)
    form = TodoForm(request.POST or None,
                    files=request.FILES or None,
                    instance=task)
    if task.user != request.user:
        return redirect('index')

    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('current')
    return render(request, 'task_view.html', {'todo': task, 'form': form})


@login_required
def current(request):
    tasks = Todo.objects.filter(user=request.user, date_completed__isnull=True)
    return render(request, 'current.html', {'todos': tasks})


@login_required
def completed(request):
    tasks = Todo.objects.filter(user=request.user,
                                date_completed__isnull=False)
    return render(request, 'completed.html', {'todos': tasks})


@login_required
def complete(request, todo_pk):
    todo = get_object_or_404(Todo, pk=todo_pk, user=request.user)
    if request.method == 'POST':
        todo.date_completed = timezone.now()
        todo.save()
        return redirect('current')

@login_required
def delete(request, todo_pk):
    todo = get_object_or_404(Todo, pk=todo_pk, user=request.user)
    if request.method == 'POST':
        todo.delete()
        return redirect('current')
