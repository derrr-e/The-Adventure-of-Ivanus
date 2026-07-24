from player import Player
from items import Item, Consumable
from weapon import Weapon

fists = Weapon.from_name('fists')

player = Player('Maks', 100, fists,)

apple = Consumable.from_name('apple')

apple.use(player)

print(player)