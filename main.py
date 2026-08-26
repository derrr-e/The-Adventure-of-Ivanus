from random import choice, randint

from mechanics.enemies import enemies, Enemy
from mechanics.player import Player
from mechanics.items import items

from locations import locations
from mechanics.sp_events import sp_event

from utilits import get_choice, change_hp, show_location, say



def random_event(player):
    event = choice([enemy, item, sp_event])
    
    return event(player) 

def test():
    while True:
        say('''
1. Бой
2. Найти предмет
3. Показать игрока
4. Создать случайное событие
5. Запустить game()
6. Запустить спец ивент
7. Сменить локацию
8. выход

''')
        
        answer = get_choice(8)
        
        actions = {
            
            1: lambda: enemy(player),
            2: lambda: item(player),
            3: lambda: print(player),   
            4: lambda: random_event(player),
            5: lambda: game(intro()),
            6: lambda: sp_event(player),
            7: lambda: game(ch_loc_menu()),
        }
        
        if answer == 8:
            break
        
        actions[answer]()
        

def enemy(player, enemy_name=None, show_intro=True):
    
    if enemy_name is None:
    
        enemy = choice(list(enemies.keys()))
    
        enemy_data = enemies[enemy] 
    
    else:
        enemy_data = enemies[enemy_name]
    
    hp = enemy_data['hp']
    enemy_dm = enemy_data['dm']
    name = enemy_data['name']
    
    art = enemy_data['art']
    
    if show_intro:
        say(f'На тебя напал {name}', 3)
    
    
    while hp > 0 and player['hp'] > 0:
        
        print(art)
        
    
        print('''Выбери действие!
1. Ударить
2. Проверить
3. Открыть инвентарь
              ''')
        
        answer = get_choice(3)
                
        if answer == 1:
            say('Ты нанес врагу 5 урона!', 1.5)
            hp -= 5
            
            say('Враг бьет тебя!')
            
            change_hp(player, -enemy_dm)
        
        
        elif answer == 2:
            print(f'Здоровье: {hp}, Урон: {enemy_dm}')
            
        elif answer == 3:
            inventory(player)

        
    if hp <= 0:
        print('Враг повержен!')
        return

    else:
        print('Ты погиб...')
        
        input('Нажмите Enter чтобы вернуться в меню')
        
        menu()
        
def menu():
    print('Добро пожаловать в The adventure of Ivanus!')
    
    say('Для выбора ответа введите цифру и нажмите Enter!')
    
    input('''Нажмите любую клавишу чтобы начать''')
    location = intro()
    if location is not None:
        game(location) 



def ch_loc(location):
    return locations[location['next']]

def ch_loc_menu():
    
    print('''
1. Таверна
2. Лес
3. Гора   
          ''')
    
    answer = get_choice(3)
    
    locs = {
        1: 'tavern',
        2: 'forest',
        3: 'mountain', 
    }

    return locs[answer]
        
        


def location_menu():
    
    print('''
1. Идти дальше
2. Отдохнуть
3. Открыть инвентарь
4. Выйти
          ''')
    
    return get_choice(4)

def intro():
    
    show_location(locations['tavern'])
    
    say('Ты видишь странного старика, который сидит совсем один...', 2.5)
    
    say('Подойдя к нему ты видишь что ему не хорошо и спрашиваешь нужна ли ему помощь', 2.5)
    
    say('Старик: Внучок, будь другом, принеси мне минералочки', 2)
    
    say('Старик: Она находится на горе с могучим орлом, я бы и сам туда зашел, но денег на лосси нет :-(', 3)
    
    say('(Лосси это лосетакси)', 1.5)
    
    print('''Согласиться или нет?
1. Конечно помогу
2. Нет, у меня своих дел полно
          ''')
    answer = get_choice(2)
    
    if answer == 2:
        print('Ты так и не узнал что у тебя могло бы быть за приключение. Может оно и к лучшему?', 3)
        return 
    
    else:
        say('Ты: Конечно помогу', 2)
        say('Старик: Спасибо', 2)
        say('Ты вышел из таверны и каким то образом сам знал куда надо идти', 3)
        
        
        return 'forest'

def game(start_location):
    
    current_location = locations[start_location]
    
    

    while not current_location.get('end', False):
        
        rested = False
        
        show_location(current_location)
        
        
             
        random_event(player)
        
        random_event(player)
        
        
        while True:
            
            answer = location_menu()

            if answer == 1:
                break
                
            elif answer == 2:
                
                if rested:
                    say('Ты уже отдыхал здесь...')
                    
                else:
                    rest(player)
                    rested = True
            
            elif answer == 3:
                inventory(player)
            
            else:
                return
            
        current_location = ch_loc(current_location)
        
        
    ending()

def ending():
    show_location(locations['mountain_top'])
    
    say('Вот и приближается конец...', 2)
    
    say('Поднявшись на вершину ты видишь Могучего Орла, который сидит за каменным столом и пьет минералку...', 2)
    
    say('Ты: Йоу чувак мне реально нужна эта минералка, дай ее плис', 2)
    
    say('Орел: Чувак ну чтобы тебе получить мою шикарную минералку ты должен доказать то, что ты ее ДЕЙСТВИТЕЛЬНО достоин', 2)
    
    say('Ты: И как же мне это сделать?', 2)
    
    say('Орел: Ты должен ответить мне на вопрос, который всю жизнь меня преследует....', 2)
    
    say('Почему скаты такие плоские?', 2)
    
    say('''
1. Потому что их плавники срослись с телом
2. Потому что их сжало давлением
3. Они по рофлу захотели стать плоскими
4. Они живут на дне и им удобнее быть плоскими
5. Я незнаю
          ''')
    
    
    actions = {
        
        3: lambda: print('Орел: Звучит клево, но нет'),
        4: lambda: print('Орел: Это правильный ответ, наверное, но тут разраб написал что правильно так что ты молодец!'),             
    }
    
    mistakes = 0
    
    while True:
        
        answer = get_choice(5)

        
        if answer == 4:
            actions[answer]()
            break
        
        elif answer == 3:
            actions[answer]()
            continue
        
        mistakes += 1

        if mistakes == 1:
            print('Орел: Ну нет')
            
        elif mistakes == 2:
            print('Орел: Знаешь, это вообще не правильный ответ')
            
        elif mistakes == 3:
            print('Орел: Я уже 200 лет сижу на этой горе и еще никто так плохо не отвечал')
            
        elif mistakes == 4:
            print('Ладно, ответ связан с тем, где они живут')

    say('Орел: Вот тебе деньги на лосси, и можешь уезжать отсюда куда хочешь!', 2)
    
    say('(Лосси это лосетакси)', 2)
    
    say('Ты взял деньги, вызвал ЛОССИ и уехал обратно в таверну где ты отдал минералку старику', 2)
    
    say('Вот так все и закончилось.... наверное?', 2)



# if __name__ == '__main__':
#     menu()