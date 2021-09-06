from django.shortcuts import render,redirect
from django.http import HttpResponse, JsonResponse
from rest_framework.parsers import JSONParser
from django.contrib.auth.models import User,auth
from django.contrib import messages
from .models import Booking
from .models import Employee
# Create your views here.
def index(request):
    employee= Employee.objects.get(pk=2)
    context={
        'employee':employee,
    }
    return render(request,'index.html',context)
def counter(request):
    text=request.POST['text']
    amount_of_words=len(text.split())
    return render(request,'counter.html', {'count': amount_of_words})
def book(request):
    if request.method == 'POST':
        username=request.POST['username']
        email=request.POST['email']
        noofpeople=request.POST['noofpeople']
        date=request.POST['date']
        time=request.POST['time']
        info=request.POST['info']
        if Booking.objects.filter(email=email).exists():
            messages.info(request,'Email Already used')
            return redirect('book')
        elif Booking.objects.filter(username=username).exists():
            messages.info(request,'Username Already exits')
            return redirect('book')
        else:
            user=Booking(username=username,email=email,noofpeople=noofpeople,date=date,time=time,info=info)
            user.save();
    return render(request,'book.html')
def data(request):
    employee= Employee.objects.all()
    student=Employee.objects.get(pk=2)
    student1=Employee.objects.get(pk=4)
    context={
        'employee':employee,
        'student':student,
        'student1':student1,
    }
    return  render(request,'data.html',context)

