from django.shortcuts import render,redirect
from .forms import TODOFORM
from .models import TODO
# Create your views here.
def task(request):
    tasks = TODO.objects.filter(created_by = request.user).order_by('-created_at')
    return render(request, 'task_list.html', {'tasks': tasks})

def task_add(request):
    if request.method == 'POST':
        form = TODOFORM(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.created_by = request.user
            task.save()
            return redirect('task')
    else:
        form = TODOFORM()
    return render(request, 'task_add.html', {'form': form})



def task_edit(request, pk):
    task = TODO.objects.get(id=pk)
    if request.method == 'POST':
        form = TODOFORM(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('task')
    else:
        form = TODOFORM(instance=task)
    return render(request, 'task_edit.html', {'form': form})



def task_delete(request, pk):
    task = TODO.objects.get(id=pk)
    task.delete()
    return redirect('task')
