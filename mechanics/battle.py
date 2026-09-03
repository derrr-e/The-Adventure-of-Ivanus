from random import choice

from mechanics.player import Player
from mechanics.enemies import Enemy
from utilits import say, get_choice
from mechanics.exeptions import LocationHasNoEnemiesError

class Battle():
    
    def __init__(self, player, enemy, start_turn='player'):
        
        self.player = player
        
        self.enemy = enemy
        
        self.rounds = 1
        
        self.current_turn = start_turn
        
    def run(self):
        
        while self.player.hp > 0 and self.enemy.hp > 0:
            
            if self.current_turn == 'player':
                
                actions = {
                    'hit': lambda: self.player.attack(self.enemy),
                    'escape': lambda: try_escape(self.player, self.enemy)
                    
                }
                
                action = yield  'need_player_action'
                
                
                result = actions[action]()
                
                
                yield result
                
            else:
                
                yield 'enemy_turn'
                
                result = self.enemy.attack(self.player)
                
                yield result
                
            self.current_turn = 'enemy' if self.current_turn == 'player' else 'player'
            
            self.rounds += 1

        else:
            
            winner = self.player if self.player.hp > 0 else self.enemy
            
            return {'message': 'Ты выиграл!' if self.player.hp > 0 else 'Ты проиграл', 'battle_over': True}
        
def try_escape(player, enemy):
    
    
    fled = True
    
    return {'fled': fled}
    

    
def interpret_result(attacker=None, target=None, damage=None, fled=None) -> dict:
    
    if fled is not None:
        
        if fled:
            return {'message': 'Ты сбежал!', 'battle_over': True}
        
        
        return {'message': 'Сбежать не удалось', 'battle_over': False}
    
    
    if isinstance(attacker, Player):
 
        if damage is not None:
            if damage:
                target.take_damage(damage)
                return {'message': f'Ты наносишь {target.name['dat']} {damage} урона', 'battle_over': False}
            
            return {'message': f'Ты промахнулся', 'battle_over': False}             
    
    elif isinstance(attacker, Enemy): 
        if damage is not None:
            if damage:
                target.take_damage(damage)
    
                return {'message': f'{attacker.name['nom']} наносит тебе {damage} урона', 'battle_over': False}
            
            return {'message': f'{attacker.name['nom']} промахивается', 'battle_over': False}
        
    return {'message': 'Ошибка: неизвестный результат боя', 'battle_over': False}
    
def show_menu():
    
    actions = {
        
        1: {'action': 'hit', 'end_turn': True},
        2: {'action': 'check', 'end_turn': False},
        3: {'action': 'open_inventory', 'end_turn': False},
        4: {'action': 'escape', 'end_turn': True},
        
        
        
    }
    print('''
1. Ударить
2. Проверить
3. Открыть инвентарь
4. Убежать
          ''')

    answer = get_choice(4)
    
    return actions[answer]

def handle_non_turn_action(action, enemy, player):
    
    actions = {
        'check': lambda: input(f'''{enemy}
                               
                            
нажми Enter чтобы выйти
                               '''),
        'open_inventory': lambda: player.open_inventory()
        
    }

    actions[action]()

def get_random_enemy(possible_enemies):
    
    key = choice(possible_enemies)
    
    return Enemy.from_name(key)

def handle_battle_outcome(player, outcome):
    say(outcome['message'])
    if outcome['battle_over']:
        return {'status': 'alive' if player.hp > 0 else 'dead'}
    return None
    
def run_battle(player, current_location, intro_title='На тебя напал {name}'):
    if current_location['enemies'] is not None:
        enemy = get_random_enemy(current_location['enemies'])
    
    else:
        raise LocationHasNoEnemiesError(current_location['name'])
    battle = Battle(player, enemy)
    
    gen = battle.run()
    
    say(intro_title.format(name=enemy.name['nom']))
    
    actions = {}
    
    
    while True:
        
        try:
            
            result = next(gen)
        except StopIteration as e:
        
            outcome = e.value
                    
            battle_result = handle_battle_outcome(player, outcome)

            return battle_result
            
        if result == 'need_player_action':
                    
                while True:
                    
                        
                    menu_result = show_menu()
                        
                    if menu_result['end_turn']:
                        
                        action_result = gen.send(menu_result['action'])     # отправляет выбор игрока в логический цикл на action = yield и принимает result

                        outcome = interpret_result(**action_result)
                        battle_result = handle_battle_outcome(player, outcome)
                        if battle_result:
                            return battle_result
                        break
                        
                    else:
                        handle_non_turn_action(menu_result['action'],  enemy, player)
                        continue
            
            
        elif result == 'enemy_turn':
            
            hit_inf = next(gen)
            
            outcome = interpret_result(**hit_inf)
            battle_result = handle_battle_outcome(player, outcome)
            if battle_result:
                return battle_result
            

            
            
            
             
    
    
