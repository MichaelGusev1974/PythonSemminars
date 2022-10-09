# 1.Напишитепрограмму, которая на вход принимать число N и выводить числа от - N до N
#
# *Примеры: *
#
# - 5 -> -5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5

# number = 0
# n = int(input('Введите число n: '))
# number = -n
# while number <= n:
#     print(number, end=', ')
#     number += 1


n = int(input('Введите число n: '))
print(list(range(-n, n + 1)))
print(*(range(-n, n + 1)))