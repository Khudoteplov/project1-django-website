from django.shortcuts import render
from django.core.cache import cache
from . import characters_db

def home(request):
    return render(request, "home.html", context={"items": characters_db.get_characters_for_table()})
