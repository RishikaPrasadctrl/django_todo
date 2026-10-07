from django.shortcuts import get_object_or_404, redirect, render
from .forms import TodoForm
from .models import Todo


def index_view(request):
  todo_list = Todo.objects.all().order_by('-created_at')
  form = TodoForm()

  if request.method == 'POST':
    form = TodoForm(request.POST)
    if form.is_valid():
      form.save()
      return redirect('index')

  context = {'todo_list': todo_list, 'form': form}
  return render(request, 'todo_app/index.html', context)


def delete_view(request, pk):
  todo = get_object_or_404(Todo, pk=pk)
  todo.delete()
  return redirect('index')


def complete_view(request, pk):
  todo = get_object_or_404(Todo, pk=pk)
  todo.completed = not todo.completed
  todo.save()
  return redirect('index')