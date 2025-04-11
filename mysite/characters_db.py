from mysite.models import Data

def get_characters_for_table():
    tab = []
    for item in Data.objects.all():
        tab.append([item.character, item.pinyin, item.tone, item.translation, item.tags])
    return tab

def write_character(new_character, new_pinyin, new_tone, new_translation):
    character = Data(character=new_character, pinyin=new_pinyin, 
                     tone=new_tone, translation=new_translation, tags="")
    character.save()

