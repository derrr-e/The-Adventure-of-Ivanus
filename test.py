from player import Player
from battle import run_battle
from items import Item, Consumable
from weapon import Weapon
from locations import locations




fists = Weapon.from_name('fists')

player = Player('Maks', 100, fists,)

apple = Consumable.from_name('apple')

current_location = locations['forest']
    
run_battle(player, current_location)