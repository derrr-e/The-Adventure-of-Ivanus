from mechanics.player import Player
from utilits import get_choice, say

def print_inventory(player):
    if not player.items:
        say('Твой инвентарь пуст')
        number = 0
    
    for number, (item, count) in enumerate(player.items, start=1):
        print(f'{number}. {player.items[item]['name']}: {count}')
    say(f'{number + 1}. Выход')
    return number
    
def answer_hadler(player, answer):
    
    