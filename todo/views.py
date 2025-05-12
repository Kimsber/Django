from django.shortcuts import render
from .models import Todo


# Create your views here.
def todo_list(request):
    todos = Todo.objects.all()
    result = {
        "todos": todos,
    }
    return render(request, "todo/todo.html", result)
