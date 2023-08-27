from random import randint

player = {
    'name': '',
    'experience': 0,
    'armor': 10,
    'hp': 50,
    'attack': 5,
    'money': 0,
    'inventory': []

}


enemies = [
    {
        'name': '(1) Бандит',
        'lvl': 1,
        'hp': 10,
        'attack': 5,
        'money_drop': randint(500, 700),
        'xp_drop': randint(10, 20),
        'win': 'Ты хороший соперник',
        'loss': 'Ты неудачник!'
    },
    {
        'name': '(2) Шестерка',
        'lvl': 5,
        'hp': 50,
        'attack': 15,
        'money_drop': randint(600, 800),
        'xp_drop': randint(40, 60),
        'win': 'Я когда нибудь выиграю тебя!',
        'loss': 'Тебе надо тренироваться.'
    },
    {
        'name': '(3) Глава бандитов',
        'lvl': 15,
        'hp': 150,
        'attack': 35,
        'money_drop': randint(700, 900),
        'xp_drop': randint(60, 80),
        'win': 'Ты слишком хорош..',
        'loss': 'Позор...'
    }
]


