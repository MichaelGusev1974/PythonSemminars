# Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент,
# второй и предпоследний и т.д.
# Пример: - [2, 3, 4, 5, 6] => [12, 15, 16];  [2, 3, 5, 6] => [12, 15]
numbers = [i for i in range(2, 9)]
print(numbers)
if len(numbers) % 2 != 0:
        for i in range(int((len(numbers) / 2) + 1)):
                print(numbers[i] * numbers[len(numbers) - i - 1], end=' ')

else:
        for i in range(int(len(numbers) / 2)):
                print(numbers[i] * numbers[len(numbers) - i - 1], end=' ')
