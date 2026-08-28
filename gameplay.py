from random import randint, choice, choices

from mechanics.player import Player
from mechanics.battle import run_battle
from utilits import say, get_choice
from presets.items_presets import items_presets
from locations import locations

def rest(player, current_location):

    
    print('Ты присел отдохнуть')

    if randint(1, 100) <= 20:
        
        run_battle(player, current_location, intro_title='Пока ты спал на тебя напал {name}')
    
        say('', 2)
        say('Это была ужасная ночь', 2)
        
        return
    
    else:
        player.heal(5)
        say('Твое здоровье пополнено на 5!')
        
        return
    
    
def find_item(player):
    
    key = choice(list(items_presets.keys()))
    data = items_presets[key].copy()
    cls = data.pop('class')
    item = cls(**data)
    
    say(f'Ты нашел {item.name}', 2)
    say(f'Взять {item.name.lower()}?', 1.5)
    
    print('''
1. Взять
2. Оставить
          ''')
    answer = get_choice(2)
    
    if answer == 1:
        player.add_item(key)
        say(f'{item.name} добавлено в твой инвентарь')
        input('Нажми Enter чтобы продолжить')
        return
    
    else:
        say('Ты просто прошел мимо')
        input('Нажми Enter чтобы продолжить')
        return
    
def location_menu():
    
    print('''
1. Идти дальше
2. Отдохнуть
3. Открыть инвентарь
4. Выйти
          ''')
    
    return get_choice(4)
    
def ch_loc(location):
    return locations[location['next']]

def sp_event(player):
    pass

def random_event(player, location):
    
    if location['event_weights'] is None:
        return
    
    event_handlers = {
        'enemy': lambda: run_battle(player, location),
        'item': lambda: find_item(player),
        'sp_event': lambda: sp_event(player)
    }
    
    weights = location['event_weights']
    
    event_type = choices(list(weights.keys()), weights=list(weights.values()))[0]
    
    return event_handlers[event_type]()