# Найдите корни квадратного уравнения АХ**2 + ВХ + С = 0, спомощью модуля. Запосите значения А,В,С 3 раза.
# Уравнения и корни запишите в файл.
from math import sqrt
def abc(a, b, c):
    D = b**2 - 4*a*c
    with open('result.txt', 'a', encoding='utf-8') as my_f_s43:
        my_f_s43.write(f'{a}x^2 + {b}x + {c} = 0\n')
        if D > 0 and a:
            my_f_s43.write(str((-b + sqrt(D))/(2*a)) + '\n')
            my_f_s43.write(str((-b - sqrt(D)) / (2 * a)) + '\n')
        elif D == 0 and b:
            my_f_s43.write(str(-b / (2 * a)) + '\n')
        else:
            my_f_s43.write('Корней нет\n')



for i in range(3):
    abc(int(input()), int(input()), int(input()))
