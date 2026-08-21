import pytest
from random import choice
from locations import locations
from mechanics.enemies import Enemy

@pytest.mark.parametrize('location', [
    
    locations['forest'],
    locations['mountain'],
    locations['mountain_top']
])
def test_enemies_with_locations_list(location):
    for _ in range(20):
        enemy = Enemy.from_name(choice(location['enemies']))

        assert enemy.preset_key in location['enemies']