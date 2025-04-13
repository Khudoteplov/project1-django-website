from django.shortcuts import render
from django.core.cache import cache
from . import characters_db
import random



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


def test(request):
    
        
    deck = characters_db.get_characters_for_table()
    current_card_number = random.randint(0, len(deck)-1)
    current_char = deck[current_card_number][0]
    current_pinyin_tone = deck[current_card_number][1] + str(deck[current_card_number][2])
    current_translation = deck[current_card_number][3]
    return render(request, "test.html", 
            context={'character': current_char, 
            'pinyin_tone': current_pinyin_tone, 'translation': current_translation})
    


    
