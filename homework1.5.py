# Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между ними
# в 2D пространстве.
# Пример:
# - A (3,6); B (2,1) -> 5,09
# - A (7,-5); B (1,-1) -> 7,21
Ax = int(input('Введите координату х точки А: '))
Ay = int(input('Введите координату y точки А: '))
Bx = int(input('Введите координату х точки B: '))
By = int(input('Введите координату y точки B: '))
distans = ((pow((Ax - Bx), 2) + pow((Ay - By), 2))) ** 0.5
print(round(distans, 2))




