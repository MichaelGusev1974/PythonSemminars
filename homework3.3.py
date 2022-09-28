# Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между
# максимальным и минимальным значением дробной части элементов.
# Пример: - [1.1, 1.2, 3.1, 5, 10.01] => 0.19
numbers = [i / 100 for i in range(5, 1111, 52)]
print(numbers)
print(f' Максимальный элемент: ', max(numbers))
print(f' Минимальный элемент: ', min(numbers))
fractional_max_part = round(max(numbers) % 1, 3)
print(f' Дробная часть максимального элемента: ', fractional_max_part)
fractional_min_part = round(min(numbers) % 1, 3)
print(f' Дробная часть минимального элемента: ', fractional_min_part)
diff = round(fractional_max_part - fractional_min_part, 2)
print(f' разницу междумаксимальным и минимальным значением дробной части элементов: ', diff)

