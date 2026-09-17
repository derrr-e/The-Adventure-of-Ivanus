from utilits import say, get_choice

from mechanics.character import Character
from mechanics.weapon import Weapon
from presets.all_items import all_items
from presets.class_map import class_map
from mechanics.exeptions import ItemNotFoundError, ItemCannotBeUsedError, ItemPresetNotFoundError
from mechanics.inventory import print_inventory
class Player(Character):
    
    def __init__(self, name,  hp, weapon, extra_damage=0):
        
        super().__init__(name, hp)
        
        self.items = {}  
        
        self.weapon = weapon

        self.extra_damage = extra_damage
    
    def add_item(self, key, count=1):
        if key not in all_items:
            raise ItemPresetNotFoundError(key)
        
        self.items[key] = self.items.get(key, 0) + count
        
    def drop_item(self, key):
        self.items[key] -= 1
        if self.items[key] <= 0:
            del self.items[key]
    
    def use_item(self, key):
        if self.items.get(key, 0 ) <= 0:
            raise ItemNotFoundError(key)
            
        try:
            data = all_items[key].copy()

        except KeyError:
            raise ItemPresetNotFoundError(key)
        
        cls_key = data.pop('class')
        cls = class_map[cls_key]
        data.pop('droppable')
        data.pop('key')
        item = cls(**data)
        
        if item.action is not None:
            item.use(self)
            
            self.items[key] -= 1
                
            if self.items[key] <= 0:
                del self.items[key] 
            return 'print_inventory'
        
        else:
            raise ItemCannotBeUsedError(key)

        
        
    def attack(self, target) -> dict: 
        
        damage = self.weapon.damage + self.extra_damage
        
        return {'attacker': self, 'target': target, 'damage': damage}

    def __str__(self):
        return f'Имя: {self.name}, Здоровье: {self.hp} '
    
        