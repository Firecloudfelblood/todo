from django.shortcuts import render, redirect
from .models import TodoModel


# Create your views here.
def todoview(request):
    mytodo = TodoModel.objects.all()
    context = {'mytodos': mytodo}
    return render(request, "todoapp/homepage.html", context)

def addtask(request):
    mytask = request.POST['task']
    TodoModel(task = mytask).save()
    return redirect(request.META['HTTP_REFERER'])

def deletetask(request, taskpk):
    TodoModel.objects.filter(id = taskpk).delete()
    return redirect(request.META['HTTP_REFERER'])

def edittaskview(request, taskpk):
    return render(request, "todoapp/edittask.html")

def edittask(request):
    task = request.POST['task']