from random import choice, randint

from mechanics.enemies import Enemy
from mechanics.player import Player
from mechanics.items import Item
from gameplay import game
from story.intro import intro
from mechanics.weapon import Weapon
from presets.weapon_presets import wearons

from locations import locations
from mechanics.sp_events import sp_event

from utilits import get_choice, change_hp, show_location, say





  
def menu():
    print('Добро пожаловать в The adventure of Ivanus!')
    
    say('Для выбора ответа введите цифру и нажмите Enter!')
    
    input('''Нажмите любую клавишу чтобы начать\n''')
    
    return intro()


def create_player():
     
    fists = Weapon.from_name('fists')
    return Player(name= "ivanus", hp= 100, weapon=fists, )


def main():
    location = menu()

    player = create_player()
    result = game(player, location)
    
    if result == 'dead':
        input('''
Игра окончена!

              
Нажми Enter чтобы вернутся в меню              
              ''')
        menu()
        
    elif result == 'quit':
        say('Выходим...', 3)
    
    elif result == 'completed':
        say('Ты прошел игру!!!!')
        
        say('Над игрой старались:')
        
        print('Der')

        return
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



if __name__ == '__main__':
    main()