from mechanics.player import Player
from mechanics.battle import run_battle
from mechanics.items import Item, Consumable
from mechanics.weapon import Weapon
from locations import locations
from gameplay import rest



fists = Weapon.from_name('fists')

player = Player('Maks', 100, fists,)

apple = Consumable.from_name('apple')

current_location = locations['forest']
    
run_battle(player, current_location)