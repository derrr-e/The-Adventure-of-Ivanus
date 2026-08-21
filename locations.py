locations = {
    "tavern": {
        "name": "Таверна",
        "description": "Тихое место, где можно отдохнуть и всегда найти собеседника",
        "next": "forest",
        "enemies": None,
    },
    "forest": {
        "name": "Лес",
        "description": "Много деревьев",
        "next": "mountain",
        "enemies": ("elf", "goblin"),
    },
    "mountain": {
        "name": "Подъем на гору",
        "description": "Осталось еще немного",
        "next": "mountain_top",
        "enemies": ("goblin",),
    },
    "mountain_top": {
        "name": "Вершина горы с могучим орлом",
        "description": "Наконец-то мы дошли до сюда.",
        "next": "",
        "enemies": ("elf",),
        "end": True,
    },
}
