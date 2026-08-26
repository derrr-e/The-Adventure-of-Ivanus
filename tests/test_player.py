import pytest

from mechanics.player import Player
from mechanics.weapon import Weapon
from mechanics.exeptions import ItemNotFoundError, ItemPresetNotFoundError, ItemCannotBeUsedError
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
       
def test_add_item_not_from_presets(player):
    with pytest.raises(ItemPresetNotFoundError):
        player.add_item('Bugatti')
            
def test_use_unused_item(player):
    player.add_item('rock')
    with pytest.raises(ItemCannotBeUsedError):
        player.use_item('rock')
        
        
