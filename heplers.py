from random import randint
from time import sleep
from data import *

def fight(current_enemy):
    round = randint(1, 2)
    enemy = enemies[current_enemy]
    enemy_hp = enemies[current_enemy]['hp']
    print(f'Противник - {enemy["name"]}')
    input('Enter чтобы продолжить')
    print()
    while player['hp'] > 0 and enemy_hp > 0:
        if round % 2 == 1:
            print(f'{player["name"]} атакует {enemy["name"]}.')
            enemy_hp -= player['attack']
            sleep(1)
        else:
            print(f'{enemy["name"]} атакует {player["name"]}.')
            player['hp'] -= enemy['attack']
            sleep(1)
        print(f'''{player['name']}: {player['hp']}
{enemy['name']}: {enemy_hp}''')
        print()
        sleep(1)
        round += 1

    if player['hp'] > 0:
        print(f'Противник - {enemy["name"]}: {enemy["win"]}')
        sleep(2)
        player['money'] += enemy['money_drop']
        player['experience'] += enemy['xp_drop']
        print(f"Вы получили {enemy['money_drop']} монет и {enemy['xp_drop']} опыта.")
        sleep(2)
        print('Вам нужно сходить потренироваться!')
        sleep(2)
        current_enemy += 1
    else:
        print(f'Противник - {enemy["name"]}: {enemy["loss"]}')
    player['hp'] = 50
    print()
    return current_enemy


def train_hp(player):
    player["hp"] += 10
    print("Тренировка завершена! Ваше здоровье увеличено на 10 единиц.")

def train_attack(player):
    player["attack"] += 5
    print("Тренировка завершена! Ваш урон увеличен на 5 единиц.")

def train_armor(player):
    player["armor"] += 2
    print("Тренировка завершена! Ваша броня увеличена на 2 единицы.")



def display_player():
    print(f'Игрок - {player["name"]}')
    print(f'''Величина атаки - {player["attack"]}. Шанс критического 
          урона ({player["attack"] * 3}ед.) равен {player["luck"]}%''')
    print(f'Броня поглощает {(1 - player["armor"]) * 100}% урона')
    print()


def display_enemy(current_enemy):
    enemy = enemies[current_enemy]
    print(f'Противник - {enemy["name"]}')
    print(f'Величина атаки - {enemy["attack"]}')
    print(f'Здоровье - {enemy["hp"]}')
    print()


def display_inventory():
    print(f'У вас есть:')
    for value in player['inventory']:
        print(value)
    print(f'{player["money"]} монет.') 



def buy_attack_potion(player):
    if player["money"] >= 1000:
        player["money"] -= 1000
        player["attack"] *= 1.25
        print("Вы купили зелье урона! Ваш урон увеличен на х1.25")
        sleep(3)
    else:
        print("У вас недостаточно монет для покупки зелья урона. Нужно 1000 монет.")
        sleep(3)

def buy_health_potion(player):
    if player["money"] >= 1000:
        player["money"] -= 1000
        player["hp"] *= 1.25
        print("Вы купили зелье здоровья! Ваше здоровье увеличено на х1.25")
        sleep(3)
    else:
        print("У вас недостаточно монет для покупки зелья здоровья. Нужно 1000 монет.")
        sleep(3)


