from arts import arts
from random import randint

from mechanics.character import Character

class Enemy(Character):
    
    
    def __init__(self, name: dict, hp: int, damage: int, key: str):
        super().__init__(name, hp)
        
        self.damage = damage
    
        self.preset_key = key

    enemy_presets = {
        
        'goblin': {'hp': (25, 30), 'damage': 5, 'name': {'nom': 'Гоблин', 'gen': 'Гоблина', 'dat': 'Гоблину'}, 'preset_key': 'goblin'},
        'elf': {'hp': (15, 20), 'damage': 7, 'name': {'nom': 'Ельф', 'gen': 'Ельфа', 'dat': 'Ельфу'}, 'preset_key': 'elf'},
        
        
        
    }
    
    def attack(self, target,):
        
        return {'attacker': self, 'target': target, 'damage': self.damage}

    def __str__(self):
        return f'Хп:{self.hp} Урон:{self.damage} Имя:{self.name['nom']}'
    
    @classmethod
    def from_name(cls, key):
        data = cls.enemy_presets[key]
        hp = randint(*data['hp'])
        return cls(data['name'], hp, data['damage'], key=key)
        

