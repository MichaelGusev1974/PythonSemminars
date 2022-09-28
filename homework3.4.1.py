# Напишите программу, которая будет преобразовывать десятичное число в двоичное.
# Пример: - 45 -> 101101; - 3 -> 11; - 2 -> 10
# 2 способ:
number = int(input('Введите число: '))
result = []
while number > 0:
    result.append(number % 2)
    number //= 2
result_revers = result[::-1]                # cпособ нарезки
print(result_revers)

number = int(input('Введите число: '))
print(bin(number))                          # метод bin() для проверки правильности вывода