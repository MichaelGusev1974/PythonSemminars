from random import *

tern = bool(randint(0, 2))
print(tern)
candys = 100
while candys > 0:
    print('осталось конфет: ', candys)
    if tern:
        candys -= int(input('Ход игрока1: '))
        tern = not tern
    else:
        candys -= int(input('Ход игрока2: '))
        tern = not tern
if tern:
    print('Победил игрок 2')
else:
    print('Победил игрок 1')
print('Game over')