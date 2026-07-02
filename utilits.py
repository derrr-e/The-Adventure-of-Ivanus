from time import sleep

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