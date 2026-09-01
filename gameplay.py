from random import randint, choice, choices

from mechanics.player import Player
from mechanics.battle import run_battle
from utilits import say, get_choice, show_location
from presets.items_presets import items_presets
from locations import locations

def rest(player, current_location):

    
    print('Ты присел отдохнуть')

    if randint(1, 100) <= 20:
        
        run_battle(player, current_location, intro_title='Пока ты спал на тебя напал {name}')
    
        say('', 2)
        say('Это была ужасная ночь', 2)
        
        return {'status': 'alive' if player.hp > 0 else 'dead'}
    
    else:
        player.heal(5)
        say('Твое здоровье пополнено на 5!')
        
        return {'status': 'alive' if player.hp > 0 else 'dead'}
    
    
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
4. Выйти (прогресс не будет сохранен!!!!!)
          ''')
    
    return get_choice(4)
    
def ch_loc(location):
    return locations[location['next']]

def sp_event(player):
    pass

def handle_location_menu(player, location):
    choice = location_menu()
    if choice == 1:
        return{'status': 'alive'}
    
    elif choice == 2:
        rest_result = rest(player, location)
        
        return rest_result

    elif choice == 3:
        player.open_inventory()
        
    else:
        return {'status': 'quit'}
    
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

def triger_random_events(player, location):
    count = randint(3, 7)
    
    for _ in range(count):
        result = random_event(player, location)
        if result and result['status'] == 'dead':
            return{'status': 'dead'}
    return{'status': 'alive'}

def game(player, start_location_key):
    current_location = locations[start_location_key]
    
    while not current_location.get('end', True):
        show_location(current_location)
        
        event_result = triger_random_events(player, current_location)
        
        if event_result['status'] == 'dead':
            return{'status': 'dead'}
        
        menu_result = handle_location_menu(player, current_location)
        if menu_result != 'alive':
            return menu_result
        current_location = ch_loc(current_location)
    
    return {'status': 'completed'}