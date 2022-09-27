# Задайте список из n чисел
# последовательности $(1+\frac 1 n)^n$ и выведите на экран их сумму.

# решение, которое нагуглил
# n = int(input('Enter number: '))
# def sequence(n):
#     return [round((1 + 1 / x) ** x, 2) for x in range(1, n + 1)]
# print(sequence(n))
# print(round(sum(sequence(n))))

# Задайте список из n чисел
# последовательности (1+\frac 1 n)^n и выведите на экран их сумму.
# мое решение:
n = int(input('Enter number: '))
result_list = []
for i in range(1, n + 1):
    s = round((1 + 1 / i)**i, 2)
    result_list.append(s)
print(result_list)
print(round(sum(result_list), 2))

