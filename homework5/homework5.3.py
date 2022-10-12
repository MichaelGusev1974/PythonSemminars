# Создайте программу для игры с конфетами человек против человека.
# Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга. Первый ход определяется
# жеребьёвкой. За один ход можно забрать не более чем 28 конфет. Все конфеты оппонента достаются забравшему последнюю конфету
# (сделавшему последний ход). Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?
# 1 Вариант
# from random import *
#
# tern = bool(randint(0, 2))
# print(tern)
# candies = 100
# while candies > 0:
#     print('осталось конфет: ', candys)
#     if tern:
#         candies -= int(input('Ход игрока1: '))
#         tern = not tern
#     else:
#         candies -= int(input('Ход игрока2: '))
#         tern = not tern
# if tern:
#     print('Победил игрок 2')
# else:
#     print('Победил игрок 1')
# print('Game over')

# 2 Вариант
from random import shuffle, randint
# CANDIES = 2021
CANDIES = 100
CANDIES_limit = 28
def bot_run(candies: int) -> int:
    result = candies % 29
    if not result:
        result = randint(1, 28)
    return result
pleyers = ["human", "bot" if int(input('play with bot 1 - yes, 0 - no')) else 'person']
shuffle(pleyers)
active_player = pleyers[0]
print(f'1 Player - {pleyers[0]}, 2 Player - {pleyers[1]}')
while CANDIES > 0:
    print(f'\nTere are {CANDIES} sweets on the table, you can take [1 .. {CANDIES_limit}')
    print(f"Player {active_player}'s move")
    if active_player == "bot":
        get_Candies = bot_run(CANDIES)
        print(f'The bot took {get_Candies} candies')
    else:
        get_Candies = int(input(f'How many candies do you want {active_player}: '))
# проверки
if get_Candies not in range(1, CANDIES_limit + 1):
    print('Wrong move')
else:
    CANDIES -= get_Candies
    if CANDIES > 0:
        if "Bot" in pleyers:
            active_player = "human" if active_player == "Bot" else "Bot"
        else:
            active_player = "human" if active_player == "Person" else "Person"
    else:
        print(f'The player {active_player} won!')