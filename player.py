from utilits import say

class Player:
    
    def __init__(self, name,  hp):
        
        self.name = name
        self.hp = hp

        self.items = {}  
        
        self.weapon = None  

    def take_damage(self, damage):
        
        self.hp -= damage

    def attack(self, enemy):
        
        if self.weapon:
            damage = self.weapon.damage
        
        else:
            damage = 1
        
        enemy.take_damage(damage)

    def __str__(self):
        return f'Имя: {self.name}, Здоровье: {self.hp} '
    
    
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
#                 say(f'Ты {self.items[item]['action'].lower()} {self.items[item]['name'].lower()}')
                
#                 change_hp(player, self.items[item]['heal'])
                
#                 self.self.items[item] -= 1
                
                
#                 if self.self.items[item] == 0:
#                     del self.self.items[item]
                
#                 input('Нажми Enter чтобы продолжить')
                
# # player = {
    
#     'hp': 100,
#     'dm': 5,
#     'items': {
        
        
        
#     },
    
    
# }