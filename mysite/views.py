from django.shortcuts import render
from django.core.cache import cache
from . import characters_db

def home(request):
    return render(request, "home.html", context={"items": characters_db.get_characters_for_table()})

def add(request):
    return render(request, "add.html")

def send(request):
    if request.method == "POST":
        cache.clear()
        new_character = request.POST.get("character")
        new_pinyin = request.POST.get("pinyin")
        new_tone = request.POST.get("tone")
        new_translation = request.POST.get("translation")
        characters_db.write_character(new_character, new_pinyin, new_tone, new_translation)
        return render(request, "home.html", context={"items": characters_db.get_characters_for_table()})
    
