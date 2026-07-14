from arts import arts
import random

class Enemy:
    
    def __init__(self, name, hp, damage):
        
        self.name = name    
        self.hp = hp
        self.damage = damage
    
    def attack(self, player):
         player.take_damage(self.damage)

    def take_damage(self, damage):
        
        self.hp -= damage

    def __str__(self):
        return f'Хп:{self.hp} Урон:{self.damage} Имя:{self.name}'
        
        



enemies = {
    
    'goblin':
{
    'hp': 30,
    'dm': 4,
    'art': 'art',
    'name': 'Гоблин'
},

    'Elf':
{
    'hp': 20,
    'dm': 3,
    'art': 'art',
    'name': 'Эльф'

},
    
}
