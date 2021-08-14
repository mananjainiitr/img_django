from django.shortcuts import render
from django.http import HttpResponse, Http404
from django.template import loader

from .models import TodoList
from .models import TodoItem
from time import sleep

# Create your views here.

def index(request):
    todolists = TodoList.objects.all()
    items = TodoItem.objects.all()
    template = loader.get_template('todo/index.html')
    context = {
        'todolists': todolists,
    }
    return render(request, 'todo/index.html', context)

def detail(request, list_id):
    try:
        todolist = TodoList.objects.get(id=list_id)
    except TodoList.DoesNotExist:
        raise Http404("This List Does not Exists")
    items_list = TodoItem.objects.filter(todo_list=todolist)
    context = {
        'todolist': todolist,
        'items_list': items_list,
        'list_id':list_id
    }
    return render(request, 'todo/details.html', context)

def create(request):
    if request.method == "GET":
        cont={"error":"",}
        return render(request, 'todo/createlist.html',cont)

    name = request.POST["name"]
    name = name.replace(" ","_")
    desc = request.POST["title"]
    due_date = str(request.POST["date"])
    print(due_date)
    due_tim = request.POST["time"]
    
    try:
        TodoList.objects.create(list_name=name)
        TodoItem.objects.create(title=desc,due_date=due_date,due_tim=due_tim,todo_list=TodoList.objects.get(list_name=name))
    except:
        cont = {"error":"Title name must be unique"}
        return render(request, 'todo/createlist.html',cont)

    lists = TodoList.objects.all()
    context = {
        'todolists': lists,

    }
    return render(request, 'todo/index.html', context)

def update(request):
    name = request.POST["name"]
    desc = request.POST["title"]
    due_tim = request.POST["time"]
    todolist = TodoList.objects.get(list_name=name)

    if(request.POST["date"]):
        due_date = request.POST["date"]
        TodoItem.objects.filter(todo_list=todolist).update(title=desc,due_tim=due_tim,due_date=due_date)
    else:
        TodoItem.objects.filter(todo_list=todolist).update(title=desc,due_tim=due_tim)
    lists = TodoList.objects.all()
    context = {
        'todolists': lists,

    }
    return render(request, 'todo/index.html', context)
def delete(request):
    name = request.POST["name"]
    todolist = TodoList.objects.get(list_name=name)
    TodoItem.objects.filter(todo_list=todolist).delete()
    TodoList.objects.filter(list_name=name).delete()
    lists = TodoList.objects.all()
    context = {
        'todolists': lists,

    }
    return render(request, 'todo/index.html', context)

