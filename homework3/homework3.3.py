# Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между
# максимальным и минимальным значением дробной части элементов.
# Пример: - [1.1, 1.2, 3.1, 5, 10.01] => 0.19
# numbers = [i / 100 for i in range(5, 1111, 52)]
# print(numbers)
#
# print(f' Максимальный элемент: ', max(numbers))
# print(f' Минимальный элемент: ', min(numbers))
#
# fractional_max_part = round(max(numbers) % 1, 3)    # остаток от деления на 1 вещественного числа прекрасно оставляет дробную часть
# print(f' Дробная часть максимального элемента: ', fractional_max_part)
#
# fractional_min_part = round(min(numbers) % 1, 3)    # остаток от деления на 1 вещественного числа прекрасно оставляет дробную часть
# print(f' Дробная часть минимального элемента: ', fractional_min_part)
#
# diff = round(fractional_max_part - fractional_min_part, 2)
# print(f' разница между максимальным и минимальным значением дробной части элементов: ', diff)
from random import uniform
def list_rund_nums(count: int):
    list_nums = []
    if count <= 0:
        print('Negative value of the number of numbers!')
        return [0.0]

    for i in range(count):
        list_nums.append(round(uniform(1, count), 2))
    return list_nums

def dif_max_min(list_nums: list):
    num_max = num_min = list_nums[0] % 1
    for i in range(1, len(list_nums)):
        num = round(list_nums[i] % 1, 2)
        if num > num_max:
            num_max = num
        elif num > num_min:
            num_min = num
    result = round((num_max - num_min), 2)
    print(f'Min:{num_min}, Max:{num_max}. Difference: {result}')
    return result

all_list = list_rund_nums(int(input('number of numbers: ')))
print(all_list)
dif_max_min(all_list)



