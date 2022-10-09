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
# n = int(input('Enter number: '))
# result_list = []
# for i in range(1, n + 1):
#     s = round((1 + 1 / i)**i, 2)
#     result_list.append(s)
# print(result_list)
# print(round(sum(result_list), 2))

# Задайте список из n чисел
# последовательности (1+\frac 1 n)^n и выведите на экран их сумму.
num = int(input('Enter number: '))
sum_nums = 0
list_nums = []
for i in range(1, num + 1):           # сдвиг диапазона числа ( от 0 до n; от 1 до n + 1; от 2 до n + 2)
    result = round((1 + 1 / i) ** i)  # если ф-я round видит дробное число, то округляет до целого: 2.2 => 2; 2.5 => 3
                                      # результат вычисления складываем в переменную result, чтоб потом можно было к result обратится
    list_nums.append(result)
    sum_nums += result

print(list_nums)
print(sum_nums)



