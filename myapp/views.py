from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import Project, Task
from django.shortcuts import get_object_or_404
# Create your views here.


def index(request):
    return HttpResponse('Index Page')

def hello(request, username):
    # print(username)
    return HttpResponse('<h1>hello %s </h1>' % username)

def about(request):
    return HttpResponse('About')

def projects(request):
    projects = list(Project.objects.all())
    return JsonResponse(projects, safe=False)

def tasks(request, id):
    tasks = get_object_or_404(Task, id=id)
    return HttpResponse('tasks,: %s' % tasks.tittle)