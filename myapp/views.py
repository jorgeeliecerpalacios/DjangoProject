from django.http import HttpResponse
from .models import Project, Task
from django.shortcuts import render, redirect, get_object_or_404
from .forms import CreateNewTask, CreateNewProject
# Create your views here.


def index(request):
    title = 'Django course!!!'
    return render(request, 'index.html', {'title': title})


def about(request):
    username = 'Jorge'
    return render(request, 'about.html', {'username': username})


def hello(request, username):
    # print(username)
    return HttpResponse('<h1>hello %s </h1>' % username)


def projects(request):
    # projects = list(Project.objects.all())
    projects = Project.objects.all()
    return render(request, 'project/projects.html', {'projects': projects})


def tasks(request):
    # tasks = Task.objects.get(title=title)
    # tasks = get_object_or_404(Task, id=id)
    tasks = Task.objects.all()
    return render(request, 'tasks/task.html', {'tasks': tasks})


def create_tasks(request):
    print('llego')
    if request.method == 'GET':
        # print('es get')
        return render(request, 'tasks/create_task.html', {'form': CreateNewTask})
        # show interface
    else:
        # print('es post')
        # print(request.GET['description'])
        # print(request.POST['title'])
        Task.objects.create(
            title=request.POST['title'], description=request.POST['description'],  project_id=2)
        return redirect('tasks')


def create_project(request):
    if request.method == 'GET':
        return render(request, 'project/create_project.html', {'form': CreateNewProject})
    else:
        project = Project.objects.create(name=request.POST['name'])
        return redirect('projects')

def project_detail(request, id):
    print(id)
    project = Project.objects.get(id=id)
    project = get_object_or_404(Project, id=id)
    tasks = Task.objects.filter(project_id=id)
    print(project)
    return render(request, 'project/detail.html',{'project': project, 'tasks': tasks})