import pytest

from mechanics.player import Player
from mechanics.weapon import Weapon
from mechanics.exeptions import ItemNotFoundError
@pytest.fixture
def player():
    sword = Weapon.from_name('sword')
    return Player(name='Test', hp=100, weapon=sword)

def test_add_item_new(player):
    player.add_item('apple')
    assert player.items['apple'] == 1
    
def test_add_item_stacks(player):
    player.add_item('apple')
    player.add_item('apple')
    assert player.items['apple'] == 2
    
def test_use_items_without_having_it(player):
    with pytest.raises(ItemNotFoundError):
       player.use_item('apple')
    