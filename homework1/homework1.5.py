# Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между ними
# в 2D пространстве.
# Пример:
# - A (3,6); B (2,1) -> 5,09
# - A (7,-5); B (1,-1) -> 7,21
Ax = int(input('Введите координату х точки А: '))
Ay = int(input('Введите координату y точки А: '))
Bx = int(input('Введите координату х точки B: '))
By = int(input('Введите координату y точки B: '))
# distans = ((pow((Ax - Bx), 2) + pow((Ay - By), 2))) ** 0.5
# print(round(distans, 2))
print(f'{((Ax - Bx) ** 2 + (Ay - By) ** 2) ** 0.5:0.4f}') # округление с  помощью f строк


# округление возможно
print(f'{8 / 7:.4}') # вывод: 1.143 - всего 4 цифры с округлением тип строка!!!!!
print(f'{8 / 7:.4f}') # вывод: 1.1429 -  4 цифры после запятой  тип строка!!!!
