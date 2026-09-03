from mechanics.items import Item
from presets.weapon_presets import wearons

class Weapon(Item):


    def __init__(self, name, description, damage):
        
        super().__init__(name, description)
        
        self.damage = damage

    @classmethod
    def from_name(cls, key):
        data = wearons[key]
        return cls(data['name'], data['description'], data['damage'])
    
fists = Weapon.from_name('fists')