import json
from typing import TypedDict, NotRequired
from random import choice
from utilits import say, get_choice, character_says


class QuizConfig(TypedDict):
    question: str
    variants: dict[str, str]
    correct_answer: int
    special_answer: NotRequired[int]
    special_reaction: NotRequired[str]
    mistake_reactions: dict[str, list[str]]
    hint: str
    win_reaction: str
    character: str

with open("presets/quiz_presets.json", encoding="utf-8") as f:
    quizzes = json.load(f)


def quiz(config: QuizConfig) -> dict[str, str]:
    mistakes = 0
    hint_was_used = False
    while True:
        say(config["question"])


        for number, variant in config["variants"].items():
            say(f"{int(number)}. {variant}", 0.25)
        answer = get_choice(len(config["variants"]))

        if answer == config["correct_answer"]:
            character_says(name=config['character'], text=config["win_reaction"])
            return {"status": "win"}

        elif (
            config.get("special_answer") is not None
            and answer == config["special_answer"]
        ):
            character_says(name=config['character'], text=config['special_reaction'])
            continue

        else:
            mistakes += 1
            if mistakes == len(config["mistake_reactions"]) + 1:
                character_says(name=config['character'], text=config['hint'])
                hint_was_used = True
                continue

            if hint_was_used:
                return {"status": "lose"}

            reaction = choice(config["mistake_reactions"][str(mistakes)])
            character_says(name=config['character'], text=reaction)