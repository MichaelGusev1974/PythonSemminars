# Напишите программу, которая на вход принимает 5  чисел и находит максимальное из них.
# Примеры:
#
# - 1, 4, 8, 7, 5 -> 8
# - 78, 55, 36, 90, 2 -> 90
# a = int (input('Введите число a: '))
# b = int (input('Введите число b: '))
# c = int (input('Введите число c: '))
# d = int (input('Введите число d: '))
# e = int (input('Введите число e: '))
#
# max1 = a
#
# if b > max1:
#     max1 = b
# if c > max1:
#     max1 = c
# if d > max1:
#     max1 = d
# if e > max1:
#     max1 = e
#
# print(max1)

# numbers = int(input(' input amount of numbers:  '))
# count = 1
# arr = []
# while( count <= numbers):
#     num = int(input(f"input {count} number: "))
#     arr.append(num)
#     count += 1
# print(arr)
# max_num = arr[0]
# for i in arr:
#     if i > max_num:
#         max_num = i
#
# print(f' max number is: {max_num}')

a = [1, 4, 8, 7, 5]
print(max(1, 4, 998, 7, 5))
