from django.shortcuts import render, redirect
from todolist.models import Task
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
import datetime
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect, JsonResponse
from django.urls import reverse
from django.core import serializers
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
@login_required(login_url='/todolist/login/')
def show_todolist(request):
    data_todolist = Task.objects.filter(user = request.user)
    context = {
    'list_data': data_todolist,
    'name': request.user,
    'last_login': request.COOKIES['last_login']
    }
    return render(request, "todolist.html", context)

def register(request):
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Akun telah berhasil dibuat!')
            return redirect('todolist:login')
    
    context = {'form':form}
    return render(request, 'register.html', context)

def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            response = HttpResponseRedirect(reverse("todolist:show_todolist"))
            response.set_cookie('last_login', str(datetime.datetime.now()))
            return response
        else:
            messages.info(request, 'Username atau Password salah!')
    context = {}
    return render(request, 'login.html', context)

def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse('todolist:login'))
    response.delete_cookie('last_login')
    return response

def create_task(request):
    if request.method == "POST":
        user = request.user
        title = request.POST.get('title')
        description = request.POST.get('description')
        task_created = Task(date=datetime.date.today(), user=user, title=title, description=description)
        task_created.save()
        return redirect('todolist:show_todolist')
    return render(request, "create-task.html")

def show_json(request):
    data_todolist = Task.objects.filter(user = request.user)
    return HttpResponse(serializers.serialize("json", data_todolist), content_type="application/json")

@login_required(login_url='/todolist/login/')
@csrf_exempt
def ajax_task(request):
    if request.method == "POST":
        user = request.user
        title = request.POST.get('title')
        description = request.POST.get('description')
        task_created = Task(date=datetime.date.today(), user=user, title=title, description=description)
        task_created.save()
        return JsonResponse({"pk" : task_created.pk, 
            "fields": {
            "date" : task_created.date,
            "user" : task_created.user,
            "title" : task_created.title,
            "description" : task_created.description
        }})