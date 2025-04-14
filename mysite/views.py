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
        characters_db.write_character(new_character, new_pinyin,
                                      new_tone, new_translation, author)
        return render(request, "home.html")

@login_required
def test(request):
    if request.method == "POST":
        char_id = int(request.POST.get("char_id"))
        result = request.POST.get("result")
        if result == "right":
            characters_db.switch_in_test(char_id)
            characters_db.incr_pinyin_cnt(char_id)
            characters_db.incr_translation_cnt(char_id)
        elif result == "pinyin":
            characters_db.reset_translation_right_cnt(char_id)
            characters_db.incr_pinyin_cnt(char_id)
        elif result == "translation":
            characters_db.incr_translation_cnt(char_id)
            characters_db.reset_pinyin_right_cnt(char_id)
        elif result == "wrong":
            characters_db.reset_translation_right_cnt(char_id)
            characters_db.reset_pinyin_right_cnt(char_id)

    test_list = characters_db.get_characters_for_test(request.user)
    if len(test_list) == 0:
        characters_db.add_all_characters_for_test(request.user)
        test_list = characters_db.get_characters_for_test(request.user)
    if len(test_list) == 0:
        return render(request, "test.html", context={"empty": True})
    if len(test_list) > 0:
        rand_numb = random.randint(0, len(test_list)-1)
        curr_char = test_list[rand_numb]
        char, pinyin, tone, translation, char_id = curr_char
        return render(request, "test.html", context={'empty': False,
            'character': char, 'pinyin_tone': pinyin+str(tone), 
            'translation': translation, 'char_id': char_id})


    
    


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
            return render(request, 'list.html', context={
                "items": characters_db.get_characters_for_table(request.user)})
        elif aim == 'active':
            characters_db.switch_activation(request.POST.get('char_id'))
            return render(request, 'list.html', context={
                "items": characters_db.get_characters_for_table(request.user)})

    return render(request, 'list.html', context={
        "items": characters_db.get_characters_for_table(request.user)})



