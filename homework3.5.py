# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
# Пример: - для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]

# Числа Фибоначчи циклом while (F(n) = F(n - 1) + F(n - 2)):
# n = int(input('Введите длину списка - число: '))
# f1 = f2 = 1
# print(f1, f2, end=' ')
#
# i = 2
# while i < n:
#     f1, f2 = f2, f1 + f2  # f1 приравнивается к f2, f2 приравнивается к f1 + f2
#     print(f2, end=' ')    # Выводится f2
#     i += 1

# Числа Фибоначчи циклом for (F(n) = F(n - 1) + F(n - 2)):
# n = int(input('Введите длину списка - число: '))
# f1 = f2 = 1
# print(f1, f2, end=' ')
#
# for i in range(2, n):
#     f1, f2 = f2, f1 + f2   # f1 приравнивается к f2, f2 приравнивается к f1 + f2
#     print(f2, end=' ')     # Выводится f2

# Рекурсивная функция последовательности чисел Фибоначчи(F(n) = F(n - 1) + F(n - 2)):
# def FibonacciRec(n):
#     if n in [1, 2]:
#         return 1
#     else:
#         return FibonacciRec(n - 1) + FibonacciRec(n - 2)
# result_list1 = []
# number1 = int(input('Введите длину списка - число: '))
# for i in range(1, number1 + 1):
#     result_list1.append(FibonacciRec(i))
# print(result_list1)

# чисел негаФибоначчи циклом for (м.б. отрицательно индексированные элементы, (F(n) = F(n + 2) - F(n + 1)):
# n = int(input('Введите длину списка - число: '))
# f1 = 1
# f2 = -1
# print(f1, f2, end=' ')
#
# for i in range(2, n):
#     f1, f2 = f2, f1 - f2   # f1 приравнивается к f2, f2 приравнивается к f1 - f2
#     print(f2, end=' ')     # Выводится f2

# def FibonacciRec(n):
#     if n in [1, 2]:
#         return 1
#     else:
#         return FibonacciRec(n - 1) + FibonacciRec(n - 2)
# def Nega_FibonacciRec(n):
#     if n == 1:
#         return 1
#     if n == 2:
#         return -1
#     else:
#         f1, f2 = 1, -1
#         for i in range(2, n):
#             f1, f2 = f2, f1 - f2
#         return f2
# result_list = [0]
# number = int(input('Введите длину списка - число: '))
# for i in range(1, number + 1):
#     result_list.append(FibonacciRec(i))
#     result_list.insert(0, Nega_FibonacciRec(i))         # Метод insert (). Вставка элемента в список в заданной позиции.
# print(result_list)                                      # Метод insert () позволяет вставить новый элемент в список из
                                                        # заданной позиции. Метод получает два параметра.
                                                        # Первый параметр – позиция вставки, которая начинается с 0.
                                                        # Второй параметр – имя объекта (значения), которое вставляется.


import math
b = abs(int(input('Введите число заначений:')))
kod = []
for i in range(-b,b+1):
    kod.append(i)
for i in range(-b-2,-len(kod)-1,-1):
    kod[i]=kod[i+2]-kod[i+1]
for i in range(b+2,len(kod),1):
    kod[i]=kod[i-2]+kod[i-1]
print(kod)


