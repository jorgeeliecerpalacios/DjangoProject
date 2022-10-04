from django.http import HttpResponse
from .models import Project, Task
from django.shortcuts import render, redirect
from .forms import CreateNewTask
# Create your views here.


def index(request):
    title = 'Django course!!!'
    return render(request,'index.html', {'title': title})

def about(request):
    username = 'Jorge'
    return render(request,'about.html', {'username': username})

def hello(request, username):
    # print(username)
    return HttpResponse('<h1>hello %s </h1>' % username)


def projects(request):
    # projects = list(Project.objects.all())
    projects = Project.objects.all()
    return render(request, 'projects.html', {'projects': projects})

def tasks(request):
    # tasks = Task.objects.get(title=title)
    # tasks = get_object_or_404(Task, id=id)
    tasks = Task.objects.all()
    return render(request,'task.html', {'tasks': tasks})

def create_tasks(request):
    print('llego')
    if request.method == 'GET':
        print('es get')
        return render(request, 'create_task.html', {'form': CreateNewTask})
   
    
        # show interface
        
    else: 
        print('es post')
        # print(request.GET['description'])
        print(request.POST['title'])
        Task.objects.create(title=request.POST['title'], description=request.POST['description'],  project_id=2)
        return redirect('/tasks/')

    
