import pytest

from mechanics.player import Player
from mechanics.weapon import Weapon
from mechanics.items import Item, Consumable


@pytest.fixture
def player():
    fists = Weapon.from_name('fists')
    return Player('Dummy', 100, fists)


def test_player_healing(player):
    
    apple = Consumable.from_name('apple')
    
    hp = player.hp
    
    apple.use(player)
    
    assert player.hp == hp +  apple.heal 
    
def test_apple_heal():
    
    apple = Consumable.from_name('apple')
    
    assert apple.heal == Consumable.presets['apple']['heal']

