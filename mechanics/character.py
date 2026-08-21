from abc import ABC, abstractmethod

class Character(ABC):
    
    def __init__(self, name, hp):
        
        self.name = name
        
        self.hp = hp
        
    def take_damage(self, amount):
        
        self.hp -= amount
    
    def heal(self, amount):
        
        self.hp += amount
    
    @abstractmethod
    def attack(self, target):
        pass
    