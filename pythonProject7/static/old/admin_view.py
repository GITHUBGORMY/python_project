from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.db.models import manager
from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render, redirect


from workshopApp.forms import LoginRegister, feedbackForm
from workshopApp.forms import workerForm,managerForm
from workshopApp.models import worker, manager, feedback



def Admin_base(request):
    return render(request, 'admin/admin_base.html')


def admin_view(request):
    data = worker.objects.all()
    return render(request , 'customer/customer_view.html',{"data":data})

def feedbacks(request):
    data = feedback.objects.all()
    return render(request, 'admin/feedbacks.html', {'data': data})


def reply_feedback(request, id):
    Feedback = feedback.objects.get(id=id)
    print(Feedback)
    if request.method == 'POST':
        r = request.POST.get('reply')
        Feedback.reply = r
        Feedback.save()
        messages.info(request, 'Reply send')
        return redirect('feedbacks')
    return render(request, 'admin/reply_feedbacks.html', {'Feedback': Feedback})