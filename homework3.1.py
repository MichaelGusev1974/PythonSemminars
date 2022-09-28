# Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной
# позиции.
# Пример: - [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12
import random
numbers = [i for i in range(15)]
print(numbers)
# random.shuffle(numbers)
# print(numbers)
summa_elements = 0
for i in range(len(numbers)):
    if i % 2 != 0:
        summa_elements += i
        print(i, end=' , ')
print(' - сумма = ', summa_elements)
