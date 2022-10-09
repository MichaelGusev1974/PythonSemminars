# Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент,
# второй и предпоследний и т.д.
# Пример: - [2, 3, 4, 5, 6] => [12, 15, 16];  [2, 3, 5, 6] => [12, 15]
# numbers = [i for i in range(2, 9)]
# print(numbers)
# if len(numbers) % 2 != 0:
#         for i in range(int((len(numbers) / 2) + 1)):
#                 print(numbers[i] * numbers[len(numbers) - i - 1], end=' ')
#
# else:
#         for i in range(int(len(numbers) / 2)):
#                 print(numbers[i] * numbers[len(numbers) - i - 1], end=' ')
from random import *
def list_rund_nums(count: int):
    if count < 0:
        print('Negative value of the number of numbers!')
        return []

    list_nums = sample(range(1, count * 2), count)
    return list_nums
def prod_pairs(list_nums: list):
    res_list = []
    len_list = len(list_nums)
    for i in range(len_list // 2):
        res_list.append(list_nums[i] * list_nums[len_list - i - 1])
    if len_list % 2:
        res_list.append(list_nums[len_list // 2])
    return res_list

all_list = list_rund_nums(int(input('number of numbers: ')))
print(all_list)
print(prod_pairs(all_list))
