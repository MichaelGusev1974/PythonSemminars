# напишите программу, которая выведет четные, нечетные  чисела последовательности:
numbers = (1, 2, 5, 7, 9, 12, 8, 6, 4, 13, 14)
print(list(filter(lambda x: not x % 2, numbers)))
print(list(filter(lambda x:  x % 2, numbers)))

print()

# напишите программу, которая выведет квадрат  чисел последовательности:
numbers = (1, 2, 5, 7, 9, 12, 8, 6, 4, 13, 14)
print(list(map(lambda x: (x, x ** 2), numbers)))

print()

# напишите программу, которая выведет квадраты нечетных, четных  чисел последовательности:
numbers = (1, 2, 5, 7, 9, 12, 8, 6, 4, 13, 14)
print(list(map(lambda x: (x, x ** 2), [x for x in numbers if x % 2])))
print(list(map(lambda x: (x, x ** 2), [x for x in numbers if not x % 2])))



