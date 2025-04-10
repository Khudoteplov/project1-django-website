from mysite.models import Data

def get_characters_for_table():
    tab = []
    for item in Data.objects.all():
        tab.append([item.character, item.pinyin, item.tone, item.translation, item.tags])
    return tab
