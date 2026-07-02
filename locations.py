locations = {
    
    'tavern':
        {
            'name': 'Таверна',
            'description': 'Тихое место, где можно отдохнуть и всегда найти собеседника',
            'next': 'forest',
        },
    'forest':
        {
            'name': 'Лес',
            'description': 'Много деревьев',
            'next': 'mountain',  
        },
        
    'mountain':
    {
        'name': 'Подъем на гору',
        'description': 'Осталось еще немного',
        'next': 'mountain_top',
    },


    'mountain_top':
        {
            'name': 'Вершина горы с могучим орлом',
            'description': 'Наконец-то мы дошли до сюда.',
            'next': '',
            'end': True
        },
}