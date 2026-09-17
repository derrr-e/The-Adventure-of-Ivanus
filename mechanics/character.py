from abc import ABC, abstractmethod

class Character(ABC):
    
    def __init__(self, name, hp):
        self.name = name
        self.hp = hp
        self.max_hp = hp
        
    def take_damage(self, amount):
        self.hp -= amount
    
    def heal(self, amount):
        self.hp = min(self.hp + amount, self.max_hp)
    
    @abstractmethod
    def attack(self, target):
        pass
    