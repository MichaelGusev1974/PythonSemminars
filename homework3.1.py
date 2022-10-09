
# Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётных
# позициях(не индексах).
# Пример: - [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12
import random
# numbers = [i for i in range(15)]
# print(numbers)
# 1
# random.shuffle(numbers)
# print(numbers)
# 2
# summa_elements = 0
# for i in range(len(numbers)):
#     if i % 2 != 0:
#         summa_elements += i
#         print(i, end=' , ')
# print(' - сумма = ', summa_elements)
from random import *
def list_rund_nums(count: int):
    if count < 0:
        print('Negative value of the number of numbers!')
        return []

    list_nums = sample(range(1, count * 2), count)
    return list_nums

def sum_odd_pos(list_nums: list):

    summa_nums = 0
    for i in range(0, len(list_nums), 2):
        summa_nums += list_nums[i]
    return summa_nums
all_list = list_rund_nums(int(input('number of numbers: ')))
print(all_list)
print(sum_odd_pos(all_list))






