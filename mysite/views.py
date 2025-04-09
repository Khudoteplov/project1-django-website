from django.shortcuts import render
from django.core.cache import cache

def home(request):
    return render(request, "home.html")
