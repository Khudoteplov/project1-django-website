from mysite.models import Characters

def get_characters_for_table(user):
    tab = []
    for item in Characters.objects.filter(user=user):
        tab.append((item.character, item.pinyin, item.tone, item.translation, item.char_id))
    return tab

def write_character(new_character, new_pinyin, new_tone, new_translation, author):
    character = Characters(character=new_character, pinyin=new_pinyin, 
                     tone=new_tone, translation=new_translation, user=author)
    character.save()


def delete_character(char_id):
    Characters.objects.filter(char_id=char_id).delete()
    
