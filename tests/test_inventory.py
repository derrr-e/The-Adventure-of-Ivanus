from pytest import fixture
from unittest.mock import patch
from mechanics.player import Player
from mechanics.weapon import Weapon
from mechanics.inventory import print_inventory

@fixture
def player():
    sword = Weapon.from_name('old_sword')
    return Player(name='Test', hp=100, weapon=sword)

def test_print_inventory_returns_chosen_key(player):
    player.add_item('apple')
    
    with patch('mechanics.inventory.get_choice', return_value=1):
        result = print_inventory(player)
        
    assert result == 'apple'