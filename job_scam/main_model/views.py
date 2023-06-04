from django.shortcuts import render, redirect
from .models import db
# Create your views here.

def home(request):
    return render(request, 'main_model/index.html', {})

def career(request):
    if request.method == 'GET':
        return render(request, 'main_model/careers.html', context={'num':0})
    else:
        data = request.POST
        try:
            instance = db.objects.create(first_name=data['first_name'],
                                         last_name=data['last_name'],
                                         email=data['email'],
                                         mobile=data['mobile'],
                                         describe=data['describe'],
                                         qualification=data['qualification'])
            return render(request, 'main_model/careers.html', context={'num':1})
        except Exception as e:
            print("In except")
            return render(request, 'main_model/careers.html', context={'num':2})