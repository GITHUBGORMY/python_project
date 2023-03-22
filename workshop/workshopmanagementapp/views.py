from django.contrib.auth import authenticate, login
from django.contrib import messages

from django.http import HttpResponse
from django.shortcuts import render, redirect


from workshopmanagementapp.forms import LoginRegister
from workshopmanagementapp.forms import workerForm


def fun(request):
    return HttpResponse(" ")
def temp(request):
    return render(request, 'modified_files/index.html')
def home(request):
    return render(request, 'home/modified_files/index.html')
def dash(request):
    return render(request, 'dash/modified_files/index.html')
def log(request):
    return render(request, 'login/modified_files/log-in.html')
def reg(request):
    return render(request, 'reg/Modified_files/index.html')
def registration(request):
    return render(request, 'register/modified_files/index.html')
def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('luname')
        password = request.POST.get('lpassword')
        user = authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            if user.is_staff:
                return redirect('home')
            elif user.is_worker:
                return redirect('dash')
            # elif user.is_user:
            #     return redirect('log-in')
        else:
            messages.info(request,'invalid credentials')
    return render(request,'login/Modified_files/log-in.html')

def worker_register(request):
    user_form = LoginRegister()
    worker_Form = workerForm()
    if request.method == 'POST':
        user_form = LoginRegister(request.POST)
        worker_Form = workerForm(request.POST)
        if user_form.is_valid() and worker_Form.is_valid():
            u=user_form.save(commit=False)
            u.is_worker =True
            u.save()
            worker = worker_Form.save(commit=False)
            worker.user = u
            worker.save()
            messages.info(request,'registration successfully complete')
            return redirect("login_view")
    return render(request,'register/Modified_files/index.html',{'user_form': user_form ,'worker_form': worker_Form})



