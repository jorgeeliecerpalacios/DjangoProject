from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import Project, Task
from django.shortcuts import get_object_or_404, render
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
    return render(request,'task.html')