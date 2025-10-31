from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

from django.http import HttpResponse

def homepage(request):
    return render(request, "index.html")

def blogpage(request):
    return render(request, "blog.html")

def show_allpage(request):
    return render(request, "show_all.html")

def aboutpage(request):
    return render(request, "about.html")