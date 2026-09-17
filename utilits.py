import select
import sys
from time import sleep
from locations import locations

def direction(value, gender):
    if value != 0:
    
        if gender == 'man':
            return 'Увеличился' if value > 0 else 'Уменьшился' 

        elif gender == 'mid':
            return 'Увеличилось' if value > 0 else 'Уменьшилось' 
            
    else:
        return

def report_hp_change(amount):

    if amount != 0:
        say(f'Твое здоровье {direction(amount, 'mid').lower()} на {abs(amount)}')
        
    return

def report_damage_change(amount):
    
    if amount != 0:
        say(f'Твой урон {direction(amount, 'man').lower()} на {abs(amount)}')
    
    return
    

       



def get_choice(max_dg):

    while True:

        answer = input(f"Введи число от 1 до {max_dg}: ")

        if answer.isdigit() and 1 <= int(answer) <= max_dg:
            return int(answer)

        print("Неверный ввод")
        
def change_hp(player, amount):
    old_hp = player['hp']
    player['hp'] += amount
    print(f"{old_hp} ---> {player['hp']} ({amount:+}) ")

def say(text='', delay = 1, skip_text=True):
    print(text)
    elapsed = 0
    while elapsed < delay:    
        readable, _, _ = select.select([sys.stdin], [], [], 0)
        if sys.stdin in readable:
            line = sys.stdin.readline()
            break
        sleep(0.1)
        elapsed += 0.1

def show_location(key):
    location = locations[key]
    say(f'{location['name']}, {location['description'].lower()}', 2)