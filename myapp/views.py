from django.shortcuts import render,redirect
from django.http import HttpResponse, JsonResponse
from rest_framework.parsers import JSONParser
from django.contrib.auth.models import User,auth
from django.contrib import messages
from .models import Employee
from .models import Department
from .models import BoardOfDirector
# Create your views here.
def index(request):
    employee= Employee.objects.all()
    employee1= Employee.objects.get(pk=1)
    employee2= Employee.objects.get(pk=2)
    employee3= Employee.objects.get(pk=3)
    employee4= Employee.objects.get(pk=4)
    employee5= Employee.objects.get(pk=5)
    employee6= Employee.objects.get(pk=6)
    employee7= Employee.objects.get(pk=7)
    employee8= Employee.objects.get(pk=8)
    employee9= Employee.objects.get(pk=9)
    departments=Department.objects.all()
    departments1=Department.objects.get(pk=1)
    departments2=Department.objects.get(pk=2)
    departments3=Department.objects.get(pk=3)
    departments4=Department.objects.get(pk=4)
    departments5=Department.objects.get(pk=5)
    directors=BoardOfDirector.objects.all()
    directors1=BoardOfDirector.objects.get(pk=1)
    directors2=BoardOfDirector.objects.get(pk=2)
    directors3=BoardOfDirector.objects.get(pk=3)
    directors4=BoardOfDirector.objects.get(pk=4)
    directors5=BoardOfDirector.objects.get(pk=5)
    directors6=BoardOfDirector.objects.get(pk=6)
    directors7=BoardOfDirector.objects.get(pk=7)
    directors8=BoardOfDirector.objects.get(pk=8)
    directors9=BoardOfDirector.objects.get(pk=9)
    context={
        'employee':employee,
        'employee1':employee1,
        'employee2':employee2,
        'employee3':employee3,
        'employee4':employee4,
        'employee5':employee5,
        'employee6':employee6,
        'employee7':employee7,
        'employee8':employee8,
        'employee9':employee9,
        'departments':departments,
        'departments1':departments1,
        'departments2':departments2,
        'departments3':departments3,
        'departments4':departments4,
        'departments5':departments5,
        'directors':directors,
        'directors1':directors1,
        'directors2':directors2,
        'directors3':directors3,
        'directors4':directors4,
        'directors5':directors5,
        'directors6':directors6,
        'directors7':directors7,
        'directors8':directors8,
        'directors9':directors9,
    }
    return render(request,'index.html',context)
def data(request):
    employee= Employee.objects.all()
    student=Employee.objects.get(pk=2)
    student1=Employee.objects.get(pk=4)
    context1={
        'employee':employee,
        'student':student,
        'student1':student1,
    }
    departments=Department.objects.all()
    context2={
        'departments':departments,
    }
    directors=BoardOfDirector.objects.all()
    context3={
        'directors':directors,
    }

    return  render(request,'data.html',context1,context2,context3)

