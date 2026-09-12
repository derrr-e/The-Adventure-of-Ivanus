from utilits import say, get_choice

from mechanics.character import Character
from mechanics.weapon import Weapon
from presets.items_presets import items_presets
from mechanics.exeptions import ItemNotFoundError, ItemCannotBeUsedError, ItemPresetNotFoundError
from mechanics.inventory import print_inventory, answer_hadler
class Player(Character):
    
    def __init__(self, name,  hp, weapon, extra_damage=0):
        
        super().__init__(name, hp)
        
        self.items = {}  
        
        self.weapon = weapon

        self.extra_damage = extra_damage
    
    def add_item(self, key, count=1):
        if key not in items_presets:
            raise ItemPresetNotFoundError(key)
        
        self.items[key] = self.items.get(key, 0) + count
        

    def use_item(self, key):
        if self.items.get(key, 0 ) <= 0:
            raise ItemNotFoundError(key)
            
        try:
            data = items_presets[key]

        except KeyError:
            raise ItemPresetNotFoundError(key)
        
        cls = data.pop('class')
        item = cls(**data)
        
        if item.action is not None:
            item.use(self)
            
            self.items[key] -= 1
                
            if self.items[key] <= 0:
                del self.items[key] 
            return
        
        else:
            raise ItemCannotBeUsedError(key)

        
        
    def attack(self, target) -> dict: 
        
        damage = self.weapon.damage + self.extra_damage
        
        return {'attacker': self, 'target': target, 'damage': damage}

    def __str__(self):
        return f'Имя: {self.name}, Здоровье: {self.hp} '
    
    def open_inventory(self):
        while True:
            number = print_inventory(self)
            answer = get_choice(number + 1)
            
#     # def open_inventory(self, ):
    
    
#         while True:
        
#             if not self.items:
#                 say("Твой инвентарь пуст", 2)
#                 return
                
#             inventory_items = list(self.items.items())
            
            
#             for number, (item, count) in enumerate(inventory_items, start=1):
#                 say(f'{number}. {self.items[item]['name']}: {count}', 1.5)
            
#             say(f'\n{number + 1}. Выход', 2)    
            
            
#             chose = get_choice(len(inventory_items) + 1)
            
            
#             if chose <= len(inventory_items):
            
#                 item, count = inventory_items[chose - 1]
            
#             else:
#                 break    
            
#             print(f'''
#         {self.items[item]['name']}
#         {self.items[item]['discription']}

#         1. {self.items[item]['action']}
#         2. Выход              
                    
#                     ''')

#             answer = get_choice(2)
            
#             if answer == 1:
#                 use_item
