from gameplay import game
from mechanics.player import Player
from mechanics.weapon import Weapon
from story.ending import ending
from story.intro import intro
from utilits import say, get_choice


def menu():
    say("Добро пожаловать в The adventure of Ivanus!", 0.5)
    say("Для выбора ответа введите цифру и нажмите Enter!")
    print("""
1. Начать игру
2. Выйти
          """)

    choice = get_choice(2)

    return {"status": "start"} if choice == 1 else {"status": "quit"}


def create_player():

    fists = Weapon.from_name("old_sword")
    return Player(
        name="ivanus",
        hp=100,
        weapon=fists,
    )


def main():
    menu_result = menu()

    if menu_result["status"] == "quit":
        say("Выходим...", 1)
        return

    elif menu_result["status"] == "start":
        intro_result = intro()

    if intro_result['status'] == 'quit':
        return

    elif intro_result['status'] == 'continue':
        player = create_player()
        result = game(player, intro_result['location'])

    if result["status"] == "dead":
        input("""
Игра окончена!

              
Нажми Enter чтобы вернутся в меню              
              """)
        menu()

    elif result["status"] == "quit":
        say("Выходим...", 1)
        return

    elif result["status"] == "completed":
        ending_result = ending()

        if ending_result["status"] == "completed":
            say("Поздравляю! Ты прошел игру!")
            input("Нажми Enter чтобы вернутся в меню")
            menu()

        elif ending_result["status"] == "dead":
            say("Ты проиграл :(")
            input("Нажми Enter чтобы вернутся в меню")
            menu()


if __name__ == "__main__":
    main()
