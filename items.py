from utilits import say, direction, report_damage_change, report_hp_change

class Item:
    
    presets = {
        
        'rock': {'name': 'Камень', 'description': 'Маленький камень, который можно найти на земле',}
        
    }
    
    def __init__(self, name, description, action=None):
        
        self.name = name

        self.description = description

        self.action = action

    def use(self, player):
        say('Ты не можешь использовать это')
    
    
    @classmethod
    def from_name(cls, key):
        data = cls.presets[key]
        return cls(**data)
    
    def __str__(self):
        return f'{self.name}.\n{self.description}'
    
    def __eq__(self, other):
        if not isinstance(other, Item):
            return False
        
        return self.name == other.name and self.description == other.description
    
class Consumable(Item):
    
    presets = {
        
        'apple': {'name': 'Яблоко', 'description': 'Сочный фрукт, который можно съесть', 'action': {'past': 'Съел', 'can_do': 'Съесть'},'heal': 5,}
        
    }
    
    
    def __init__(self, name, description, action, heal=0, damage=0):
        super().__init__(name, description, action)

        self.heal = heal

        self.damage = damage
    
    def use(self, player):
        
        
        say(f'Ты {self.action['past'].lower()} {self.name}')
        
        report_hp_change(self.heal)
        
        report_damage_change(self.damage)
                    
        player.heal(self.heal)
        
        player.extra_damage += self.damage
        
            
    
    
    def __eq__(self, other):
        if not isinstance(other, Consumable):
            return False
        
        return super().__eq__(other) and self.heal == other.heal and self.damage == other.damage





