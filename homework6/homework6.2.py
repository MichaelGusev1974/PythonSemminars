# Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент,
# второй и предпоследний и т.д.
# 1 Четное кол-во элементов
numbers = [i for i in range(2, 8)]
print(numbers)
print(list(map(lambda x: (numbers[x] * numbers[len(numbers) - x - 1]), [x for x in range(len(numbers) // 2)])))

print()

# 1 Нечетное кол-во элементов
numbers = [i for i in range(2, 9)]
print(numbers)
print(list(map(lambda x: (numbers[x] * numbers[len(numbers) - x - 1]), [x for x in range((len(numbers) // 2) + 1)])))