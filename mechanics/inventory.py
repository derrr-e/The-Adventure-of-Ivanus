from mechanics.items import Item, Consumable
from presets.class_map import class_map
from utilits import get_choice, say
from presets.all_items import all_items

def print_inventory(player):
    if not player.items:
        say('Твой инвентарь пуст')
        number = 0
        input('Нажми Enter чтобы выйти')
        return 'exit'
        
    options = {}
    for number, (key, count) in enumerate(player.items.items(), start=1):
        item_data = all_items[key]
        print(f'{number}. {item_data['name']}: {count}')
        options[number] = key
    
    exit_number = len(options) + 1
    options[exit_number] = 'exit'
    print(f'{exit_number}. Выход')
    option = get_choice(exit_number)
    
    return options[option]
    

def option_handler(player, option):
    if option == 'exit':
        return option
    else:
        return option # передает ключ в печать возможных действий

def print_item_action(player, key):
    item_data = all_items[key]

    action_labels = {
        'drop': 'Выбросить',
        'exit': 'Выход'    
    }
    
    available_actions = []
    if item_data['action'] is not None:
        available_actions.append('use')
        action_labels['use'] = item_data['action']
        
    if item_data['droppable']:
        available_actions.append('drop')
    
    available_actions.append('exit')
    
    
    actions = {}
    for number, action in enumerate(available_actions, start=1):
        if action == 'use':
            print(f'{number}. {action_labels[action]['present']}')    
        else:
            print(f'{number}. {action_labels[action]}')
        actions[number] = action
    
    answer =  get_choice(len(actions))
    return {'action': actions[answer], 'key': key}

def item_action_handler(player, key, action):
    if action == 'exit':
        return 'print_inventory'
    
    item_data = all_items[key]
    actions = {
        'use': lambda: player.use_item(key),
        'drop': lambda: drop_item(player, key),
    }
    return actions[action]()
    

def drop_item(player, key):
    item_data = all_items[key]
    
    print(f'''Ты уверен что хочешь выбросить {item_data['name']}?
    (ты не сможешь его потом вернуть!!!!)
    
1. Да
2. Нет
          ''')
    
    answer = get_choice(2)
    if answer == 1:
        player.drop_item(key)
        return 'print_inventory'
    else:
        return 'print_item_actions'
    

def open_inventory(player):
    
    while True:
        answer = print_inventory(player)
        if answer == 'exit':
            return

        option = option_handler(player, answer)
        
        while True:
            action = print_item_action(player, option)
            
            result = item_action_handler(player=player, **action)
            
            
            if result == 'print_inventory':
                break
        