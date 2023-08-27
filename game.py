from random import*
from time import*
from data import*
from heplers import*

name = input('Введи свой никнейм: ')
player['name'] = name
current_enemy = 0

while True:
    action = input('''Выберите действие:
1 - в бой
2 - тренировка
3 - магазин
4 - показать инвентарь
5 - информация о игроке
6 - информация о текущем враге
7 - Выход
''')
    if action == 'break':
        break
    if action == '1':
        current_enemy = fight(current_enemy)
        if current_enemy == 3:
            break
    elif action == "2":
        while True:
            print("1. Тренировка здоровья")
            print("2. Тренировка урона")
            print("3. Выход")

            choice = input("Выберите действие: ")

            if choice == "1":
                train_hp(player)
                sleep(0.5)
            elif choice == "2":
                train_attack(player)
                sleep(0.5)
            elif choice == "3":
                print("До свидания!")
                sleep(0.5)
            break
    elif action == "3":
        while True:
            print("1. Купить зелье урона")
            print("2. Купить зелье здоровья")
            print("3. Выход")

            choice = input("Выберите действие: ")

            if choice == "1":
                buy_attack_potion(player)
            elif choice == "2":
                buy_health_potion(player)
            elif choice == "3":
                print("До свидания!")
            break
    elif action == '4':
        display_inventory()
        sleep(3)
    elif action == '5':
        print(player)
        sleep(3)
    elif action == '6':
        print(current_enemy)
        sleep(3)
    elif action == '7':
        print('До свидания!')
        break
    else:
        print('Что-то пошло не так')
