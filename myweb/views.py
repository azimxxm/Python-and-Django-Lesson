import requests
from django.shortcuts import render, redirect
from .models import DataBase
from .forms import DataBaseForm

def home(request):
    return render(request, 'main/home.html')

def about(request):
    return render(request, 'main/about.html')

def contact(request):
    return render(request, 'main/contact.html')

def news_home(request):
    news = DataBase.objects.all()
    return render(request, 'main/news_home.html', {'news':news})

def create(request):
    error = ''
    if request.method == "POST":
        form = DataBaseForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            error = 'Create not full'


    form = DataBaseForm()

    data = {
        'form':form,
        'error': error
    }
    return render(request, 'main/create.html', data)