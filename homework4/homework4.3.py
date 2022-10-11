# Задайте последовательность чисел. Напишите программу, которая выведет список неповторяющихся элементов исходной
# последовательности.
# 1. способ:
# def unique_elements(list):
#     list = set(list)
#     return list
# sequence_of_numbers = [-3, -2, -1, 0, 0, 0, 1, 2, 3, 3, 3, 4, 5, 6, 6, 7, 8, 8, 8, 9, 10, 11]
# print(sequence_of_numbers)
#print(sorted(unique_elements(sequence_of_numbers)))

# 2. способ:
# sequence_of_numbers = set(sequence_of_numbers)
# print(sorted(sequence_of_numbers))
# 3. способ:
# from more_itertools import unique_everseen
#     items = [1, 2, 0, 1, 3, 2]
#     list(unique_everseen(items))
#     [1, 2, 0, 3]
# 4. способ:
# from collections import OrderedDict
# items = [1, 2, 0, 1, 3, 2]
# list(OrderedDict.fromkeys(items))
# [1, 2, 0, 3]
# 4. способ:
# def unique_elements(list):
#     new_list = []
#     for i in numbers:
#         if i not in new_list:
#             new_list.append(i)
#     return new_list
#
# numbers = [-3, -2, -1, 0, 0, 0, 1, 2, 3, 3, 3, 4, 5, 6, 6, 7, 8, 8, 8, 9, 10, 11]
# print(numbers)
# print(unique_elements(numbers))
# Первые четыре способа - элементы уникальны, но вывод и повторяющихся.
# Задайте последовательность чисел. Напишите программу, которая выведет список неповторяющихся элементов исходной
# последовательности.
# 1 способ
# list = [5, 6, 8, 5, 8, 10]
# list1 = []
# count = 0
# for i in range(len(list)):
#     print(i)
#     while count < len(list):
#         if list[count] == list[i] and count != i:
#             print(count, i)
#             count = 0
#             break
#         count += 1
#     else:
#         list1.append(list[i])
#         count = 0
# print(list1)

# 2 способ
from random import randrange
def list_rund_nums(count: int):
    if count < 0:
        print('Negative value of the number of numbers!')
        return []
    list_nums = []
    for i in range(count):
        list_nums.append(randrange(count))
    return list_nums
def uniq_el(list_nums:list):
    result = []
    my_dict = {}.fromkeys(list_nums, 0) # создали словарь, ключами которого являются числа последовательности list_nums
    for i in list_nums:
        my_dict[i] += 1
    for k in my_dict:
        if my_dict[k] == 1:
            result.append(k)
    return result
all_list = list_rund_nums(int(input('number of numbers: ')))
print(all_list)
print(uniq_el(all_list))







