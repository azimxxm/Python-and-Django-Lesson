from django.shortcuts import render
from .models import DataBase

def home(request):
    return render(request, 'main/home.html')

def about(request):
    return render(request, 'main/about.html')

def contact(request):
    return render(request, 'main/contact.html')

def news_home(request):
    news = DataBase.objects.all()
    return render(request, 'main/news_home.html', {'news':news})