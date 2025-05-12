from django.shortcuts import render
from .models import Todo


# Create your views here.
def todo_list(request):
    todos = Todo.objects.all()
    # get(唯一值，ex: id，使用時須注意前端、物件型態); filter(多數，必為容器型態)
    # todos = Todo.objects.filter(important=True)
    result = {
        "todos": todos,
    }
    return render(request, "todo/todo.html", result)


def viewtodo(request, id):
    todo = None
    try:
        todo = Todo.objects.get(id=id)
    except Exception as e:
        print(e)

    return render(request, "todo/viewtodo.html", {"todo": todo})
