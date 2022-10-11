# Задана натуральная степень k. Сформировать случайным образом список коэффициентов (значения от 0 до 100)
# многочлена и записать в файл многочлен степени k.
# Пример:
# - k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0

# 1 вариант:

# from random import *
# k = 2
# a = round(random()*10)
# b = round(random()*10)
# c = round(random()*10)
# print(a, b, c)
#
# result = ''
# if b == 0: result = f'{a}*x**{k} + {c}*x**{k-2} = 0'
# if b == 0 and c == 0: result = f'{a}*x**{k} = 0'
# if c == 0: result = f'{a}*x**{k} + {b}*x**{k-1} = 0'
# else: result = f'{a}*x**{k} + {b}*x**{k-1} + {c}*x**{k-2} = 0'
# print(result)
# with open('file_hw44.txt', 'w' ) as file_hw44:
#     file_hw44.write(result)

# 2 вариант:
from random import *
def polynomyil(num: int):
    if num < 1:
        return 0
    poly = ''
    num_list = range(0, 10)
    with open('poly.txt', "a", encoding='utf-8') as my_f:
        for i in range(num, 0, -1):
            value = choice(num_list)
            if value:
                poly += f"{value}*x^{i} {choice('+-')}"
        my_f.write(f"{poly}{choice(num_list)} = 0\n")

for i in range(3):
    print(polynomyil(int(input())))
