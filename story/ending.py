from utilits import say, get_choice, show_location
from locations import locations
import json
from mechanics.quiz import quiz, quizzes

with open("presets/ending_parts.json", encoding="utf-8") as f:
    ending_parts = json.load(f)


def play_lines(lines: list[dict]) -> None:
    for line in lines:
        say(line["text"], line["delay"])


def intro_part():
    show_location("mountain_top")
    play_lines(ending_parts["intro"])


def win_outro():
    play_lines(ending_parts["win_outro"])


def lose_outro():
    play_lines(ending_parts["lose_outro"])


def ending():
    intro_part()
    result = quiz(quizzes["eagle_quiz"])

    if result["status"] == "win":
        win_outro()
        return {"status": "completed"}

    elif result["status"] == "lose":
        lose_outro()
        return {"status": "dead"}
