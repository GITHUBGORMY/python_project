from django.shortcuts import render, redirect

# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
import ToDo
from ToDoApp.forms import ToDoForm
from ToDoApp.models import Todo


def fun(request):
    return HttpResponse(" ")
def temp(request):
    return render(request, 'modified_files/index.html')
def temp2(request):
    return render(request, 'temp2/Modified_files/dashindex.html')
#create TodoApp
def adddata(request):
    form=ToDoForm()
    if request.method =="POST":
        form=ToDoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('view')
    return render(request,'demo.html',{"form":form})
def exte(request):

  return render(request,'temp2/Modified_files/dashindex.html')

#read/view
def view(request):
    data = Todo.objects.all()
    return render(request,'temp2/adddata.html',{"data":data})
#delete function
def delete(request,id):
    data = Todo.objects.get(id=id)
    data.delete()
    return redirect('view')
def update(request,id):
    todo =Todo.objects.get(id=id)
    form = ToDoForm(instance=todo)
    if request.method == 'POST':
        form = ToDoForm(request.POST,instance=todo)
        if form.is_valid():
            form.save()
            return redirect('view')

    return render(request,'update.html',{'form':form})

