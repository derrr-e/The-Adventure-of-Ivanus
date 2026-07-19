from arts import arts
from random import randint

from character import Character

class Enemy(Character):
    
    
    def __init__(self, name, hp, damage):
        super().__init__(name, hp)
        
        self.damage = damage
    
    enemy_presets = {
        
        'goblin': {'hp': (25, 30), 'damage': 5, 'name': 'Гоблин'},
        'elf': {'hp': (15, 20), 'damage': 7, 'name': 'Ельф'},
        
        
        
    }
    
    def attack(self, target,):
        target.take_damage(self.damage)
        
        return self.damage

    def __str__(self):
        return f'Хп:{self.hp} Урон:{self.damage} Имя:{self.name}'
    
    @classmethod
    def from_name(cls, key):
        data = cls.enemy_presets[key]
        hp = randint(*data['hp'])
        return cls(data['name'], hp, data['damage'])
        

