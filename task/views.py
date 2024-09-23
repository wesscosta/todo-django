from django.shortcuts import get_object_or_404, redirect, render
from task.forms import TaskForm
from task.models import Task

def task_list(request):
  tasks = Task.objects.all()
  return render(request, 'tasks/task_list.html', {'tasks': tasks})


# Criar Tarefas
def task_create(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('task_list')
    else:
        form = TaskForm()
    return render(request, 'tasks/task_create.html', {'form': form})

# Atualizar Tarefas
def task_update(request, pk):
    task = get_object_or_404(Task, pk=pk)
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('task_list')
    else:
      form = TaskForm(instance=task)
      return render(request, 'tasks/task_update.html', {'form': form, 'task': task})

def task_delete(request, pk):
  task = get_object_or_404(Task, pk=pk)
  if request.method == 'POST':
    task.delete()
    return redirect('task_list')
  return render(request, 'tasks/task_delete.html',  {'task':task})
