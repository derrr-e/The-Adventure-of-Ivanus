from mechanics.items import Item, Consumable

items_presets = {
    
    'rock': {'class': Item, 'name': 'Камень', 'description': 'Обычный камень, который можно найти на любой дороге',  'action': 'Ты не можешь использовать этот предмет', 'can_use': False},
    'apple': {'class': Consumable, 'name': 'Яблоко', 'description': 'Сочный фрукт, который может восполнить немного здоровья', 'action': {'past': 'Съел', 'present': 'Сьесть'}, 'heal': 5, 'can_use': True} # '': {'class': Consumable, 'name': '', 'description': '', 'action': {'past': '', 'present': ''}, 'heal': , 'can_use': }  
    
    
    
}