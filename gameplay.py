from random import randint

from mechanics.player import Player
from mechanics.battle import run_battle
from utilits import say


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
    
    say('Ты нашел предмет!', 1.5) 
    say(f'Это {item_name}')
    
    print(f'''Взять {item_name}?
1. Взять
2. Пусть дальше валяется''')
    
    answer = get_choice(2)