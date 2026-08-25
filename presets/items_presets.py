from mechanics.items import Item, Consumable

items_presets = {
    
    'rock': {'class': Item, 'name': 'Камень', 'description': 'Обычный камень, который можно найти на любой дороге',},
    'apple': {'class': Consumable, 'name': 'Яблоко', 'description': 'Сочный фрукт, который может восполнить немного здоровья', 'action': {'past': 'Съел', 'present': 'Сьесть'}, 'heal': 5} # '': {'class': Consumable, 'name': '', 'description': '', 'action': {'past': '', 'present': ''}, 'heal': }  
    
    
    
}