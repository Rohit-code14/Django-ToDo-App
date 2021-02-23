from django.shortcuts import render,redirect
from .models import task
# Create your views here.


def addTask(request):
    if request.method == 'POST':
        taskObj= task(name= request.POST['taskname'],date= request.POST['taskdate'])
        taskObj.save()
        return redirect('/')
    return render(request,'add.html')

def home(request):
    obj = task.objects.all()


    return render(request , 'index.html' ,{"obj":obj})

def deleteTask(request,taskId):
    taskobj = task.objects.get(id=taskId)
    if request.method == "POST":
        taskobj.delete()
        return redirect('/')
    
    return render(request,'del.html')

def editTask(request,taskId):
    taskobj = task.objects.get(id=taskId)

    if request.method=="POST":
        taskobj.name = request.POST['taskname']
        taskobj.date = request.POST['taskdate']
        taskobj.save()
        return redirect('/')

    return render(request,'edit.html',{"taskobj":taskobj})