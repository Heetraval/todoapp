from django.shortcuts import render
from django.utils import timezone
from .models import Todo
from django.http import HttpResponseRedirect


def home(request):
    todo_items = Todo.objects.all().order_by("-added_date")
    return render(request, 'index.html', {"todo_items": todo_items})

def add(request):
    cur_date = timezone.now()
    #print(request.POST)
    content = request.POST['content']
    created_obj = Todo.objects.create(added_date=cur_date, text=content)
    #print(created_obj)
    #print(created_obj.id)
    len_of_todo = Todo.objects.all().count()
    #print(len_of_todo)

    added_date = timezone.now()




    return render(request, 'todoapp/add.html')


# Create your views here.
def deltodo(request, todo_id):
    Todo.objects.get(id=todo_id).delete()
    #print(todo_id)
    return HttpResponseRedirect("/")

