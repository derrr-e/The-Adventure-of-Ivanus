from mechanics.items import Item
from presets.weapon_presets import wearons

class Weapon(Item):


    def __init__(self, name, description, damage):
        
        super().__init__(name, description)
        
        self.damage = damage

    @classmethod
    def default(cls):
        return cls('Кулаки', 'Голые руки, которые не очень хороши в бою', 1)

    @classmethod
    def from_name(cls, key):
        data = wearons[key]
        return cls(data['name'], data['description'], data['damage'])
    
