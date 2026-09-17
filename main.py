from random import choice, randint

from mechanics.enemies import Enemy
from mechanics.player import Player
from mechanics.items import Item
from gameplay import game
from story.intro import intro
from mechanics.weapon import Weapon
from presets.weapon_presets import wearons

from locations import locations
from mechanics.sp_events import sp_event

from utilits import get_choice, change_hp, show_location, say





  
def menu():
    print('Добро пожаловать в The adventure of Ivanus!')
    
    say('Для выбора ответа введите цифру и нажмите Enter!')
    
    input('''Нажмите любую клавишу чтобы начать\n''')
    
    return intro()


def create_player():
     
    fists = Weapon.from_name('fists')
    return Player(name= "ivanus", hp= 100, weapon=fists, )


def main():
    location = menu()

    player = create_player()
    result = game(player, location)
    
    if result == 'dead':
        input('''
Игра окончена!

              
Нажми Enter чтобы вернутся в меню              
              ''')
        menu()
        
    elif result == 'quit':
        say('Выходим...', 3)
    
    elif result == 'completed':
        say('Ты прошел игру!!!!')
        
        say('Над игрой старались:')
        
        print('Der')

        return


if __name__ == '__main__':
    main()