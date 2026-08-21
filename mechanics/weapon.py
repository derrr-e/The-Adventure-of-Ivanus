from mechanics.items import Item

class Weapon(Item):

    wearons = {
        'fists': {'name': 'Кулаки', 'damage': 1, 'description': 'Обычные кулаки, которые есть почти у всех'},
        'stick': {'name': 'Палка', 'damage': 5, 'description': 'Палка, которая раньше была частью какого то дерева, но сейчас ее можно использовать как оружие!'},
        'sword': {'name': 'Меч', 'damage': 10, 'description': 'Древний меч'},
        'God_sword': {'name': 'Меч бога', 'damage': 999999, 'description': 'ема что это'},
    }

    def __init__(self, name, description, damage):
        
        super().__init__(name, description)
        
        self.damage = damage

    @classmethod
    def from_name(cls, key):
        data = cls.wearons[key]
        return cls(data['name'], data['description'], data['damage'])
    
fists = Weapon.from_name('fists')