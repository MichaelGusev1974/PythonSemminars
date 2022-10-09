#Напишите программу, которая по заданному номеру четверти, показывает диапазон возможных
# координат точек в этой четверти (x и y).
quterNumder = int(input('Введите номер четверти в декартовой координатной плоскости: '))

if (quterNumder == 1):
    print('Диапазон: x: от 0 до + infinity,  y: от 0 до + infinity;')
elif (quterNumder == 2):
    print('Диапазон: x: от - infinity до 0,  y: от 0 до + infinity;')
elif (quterNumder == 3):
    print('Диапазон: x: от  - infinity до 0,  y: от  - infinity до 0;')
elif (quterNumder == 4):
    print('Диапазон: x: от 0 до + infinity,  y: от  - infinity до 0;')
else:
     print('Ввели неправильный номер четверти (от 1 до 4)')