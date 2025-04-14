from mysite.models import Characters

def get_characters_for_table(user):
    tab = []
    for item in Characters.objects.filter(user=user):
        tab.append((item.character, item.pinyin, item.tone, item.translation, item.char_id, item.pinyin_right_cnt, item.translation_right_cnt, item.active))
    return tab

def write_character(new_character, new_pinyin, new_tone, new_translation, author):
    character = Characters(character=new_character, pinyin=new_pinyin, 
                     tone=new_tone, translation=new_translation, user=author)
    character.save()


def delete_character(char_id):
    Characters.objects.filter(char_id=char_id).delete()
    

def get_characters_for_test(user):
    tab = []
    for item in Characters.objects.filter(user=user, in_test=True):
        tab.append((item.character, item.pinyin, item.tone, item.translation, item.char_id))
    return tab

def add_all_characters_for_test(user):
    for item in Characters.objects.filter(user=user, active=True):
        setattr(item, 'in_test', True)
        item.save()


def start_test(user):
    for item in Characters.objects.filter(user=user, active=True, in_test=False):
        item.switch_in_test()
    return get_characters_for_test()

def switch_in_test(char_id):
    obj = Characters.objects.get(char_id=char_id)
    t = getattr(obj, 'in_test')
    setattr(obj, 'in_test', not t)
    obj.save()

def activate(char_id):
    obj = Characters.objects.get(char_id=char_id)
    setattr(obj, 'active', True)
    obj.save()

def deactivate(char_id):
    obj = Characters.objects.get(char_id=char_id)
    setattr(obj, 'active', False)
    obj.save()

def switch_activation(char_id):
    obj = Characters.objects.get(char_id=char_id)
    t = getattr(obj, 'active')
    setattr(obj, 'active', not t)
    setattr(obj, 'in_test', not t)
    obj.save()

def reset_pinyin_right_cnt(char_id):
    obj = Characters.objects.get(char_id=char_id)
    setattr(obj, 'pinyin_right_cnt', 0)
    obj.save()


def reset_translation_right_cnt(char_id):
    obj = Characters.objects.get(char_id=char_id)
    setattr(obj, 'translation_right_cnt', 0)
    obj.save()

def incr_pinyin_cnt(char_id):
    obj = Characters.objects.get(char_id=char_id)
    t = getattr(obj, 'pinyin_right_cnt')
    setattr(obj, 'pinyin_right_cnt', t+1)
    obj.save()

def incr_translation_cnt(char_id):
    obj = Characters.objects.get(char_id=char_id)
    t = getattr(obj, 'translation_right_cnt')
    setattr(obj, 'translation_right_cnt', t+1)
    obj.save()

