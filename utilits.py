from time import sleep

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
        say(f'Твое здоровье {direction(amount, 'mid')} на {abs(amount)}')
        
    return

def report_damage_change(amount):
    
    if amount != 0:
        say(f'Твой урон {direction(amount, 'man')} на {abs(amount)}')
    
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

text_delay = 1

def say(text='', delay = 1):
    print(text)
    
    if text_delay > 0:
        sleep(delay * text_delay)

def show_location(location):
    say(f'{location['name']}, {location['description'].lower()}', 2)