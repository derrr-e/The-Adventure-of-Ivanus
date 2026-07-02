from random import choice

from utilits import get_choice, change_hp, say

def well(player):
    say('Ты нашел колодец!', 1.5)
    
    print('''Выбери действие:
1. Выпить воды из него
2. Пройти мимо
          ''')
    answer = get_choice(2)
    
    if answer == 1:
        print('''Вода из колодца делает тебя бодрее!''')
        
        change_hp(player, +5)
    

sp_events = [
    
    well,
    
    
]
    
    
    
    


def sp_event(player):
    
    choice(sp_events)(player)