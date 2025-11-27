from django.shortcuts import render, redirect, get_object_or_404
from .models import Todo

# Create your views here.
def todo_list(request):
    todos = Todo.objects.all().order_by('-created_date')
    return render(request, 'todo/todo_list.html', {'todos': todos})

def todo_create(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description')
        due_date = request.POST.get('due_date')
        if due_date == '':
            due_date = None
            
        Todo.objects.create(
            title=title,
            description=description,
            due_date=due_date
        )
        return redirect('todo_list')
    return render(request, 'todo/todo_form.html')

def todo_update(request, pk):
    todo = get_object_or_404(Todo, pk=pk)
    if request.method == 'POST':
        todo.title = request.POST.get('title')
        todo.description = request.POST.get('description')
        due_date = request.POST.get('due_date')
        if due_date == '':
            todo.due_date = None
        else:
            todo.due_date = due_date
        
        todo.completed = request.POST.get('completed') == 'on'
        todo.save()
        return redirect('todo_list')
    return render(request, 'todo/todo_form.html', {'todo': todo})

def todo_delete(request, pk):
    todo = get_object_or_404(Todo, pk=pk)
    if request.method == 'POST':
        todo.delete()
        return redirect('todo_list')
    return render(request, 'todo/todo_confirm_delete.html', {'todo': todo})
