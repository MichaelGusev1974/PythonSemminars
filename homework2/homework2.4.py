# Задайте список из N элементов, заполненных числами из промежутка [-N, N].
# Найдите произведение элементов на указанных позициях. Позиции хранятся в файле file.txt в одной строке одно число.
# n = int(input('Задайте список числа n: '))
# position_one = int(input('Позиция1: '))
# position_two = int(input('Позиция2: '))
# listing = []
# for i in range(-n, n + 1):
#     listing.append(i)
# print(listing)
# print(listing[position_one - 1] * listing[position_two - 1])

num = int(input('Enter the value of n: '))
n_1 = int(input('position_one: '))
n_2 = int(input('position_two: '))
nums_list = list(range(-num, num + 1))
print(nums_list)

len_list = len(nums_list)
if len_list >= n_1 > 0 and len_list >= n_1 > 0:
    print(nums_list[n_1 - 1] * nums_list[n_2 - 1])
else:
    print('There are no values for these indexes')