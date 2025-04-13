from django.shortcuts import render, redirect
from django.core.cache import cache
from . import characters_db
import random
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required


def home(request):
    return render(request, "home.html")

@login_required
def add(request):
    return render(request, "add.html")

@login_required
def send(request):
    if request.method == "POST":
        cache.clear()
        new_character = request.POST.get("character")
        new_pinyin = request.POST.get("pinyin")
        new_tone = request.POST.get("tone")
        new_translation = request.POST.get("translation")
        author = request.user
        characters_db.write_character(new_character, new_pinyin, new_tone, new_translation, author)
        return render(request, "home.html", 
                      context={"items": characters_db.get_characters_for_table(request.user)})

@login_required
def test(request):
    deck = characters_db.get_characters_for_table(request.user)
    current_card_number = random.randint(0, len(deck)-1)
    current_char = deck[current_card_number][0]
    current_pinyin_tone = deck[current_card_number][1] + str(deck[current_card_number][2])
    current_translation = deck[current_card_number][3]
    return render(request, "test.html", 
            context={'character': current_char, 
            'pinyin_tone': current_pinyin_tone, 'translation': current_translation})
    


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'registration/register.html', {'form': form})
    


@login_required
def list(request):
    if request.method == 'POST':
        aim = request.POST.get("aim")
        if aim == 'delete':
            characters_db.delete_character(request.POST.get('char_id'))
            return render(request, 'list.html', 
                    context={"items": characters_db.get_characters_for_table(request.user)})

    return render(request, 'list.html', context={"items": characters_db.get_characters_for_table(request.user)})



