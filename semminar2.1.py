# Напишите программу, которая принимает на вход число N и выдаёт последовательность из N членов.
# *Пример:*          - Для N = 5: 1, -3, 9, -27, 81
# n = int(input('Введите число: '))
# element = -3
# for i in range(n):
#     print(element**i, end = ', ')
# в данной задаче число n перебирается в цикле от 0 до n. На каждой итерации значение i есть показатель степени, в которую
# возводится element.
#  числа не итерабельны, в отличие от строки, списка (любой последовательности). Нужно применять ф-ю range()(работает только с целыми числами)

n = int(input('Введите число: '))
num = 1
for i in range(n):
    print(num, end='  ')
    num *= -3
