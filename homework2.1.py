
# cсумма цифр натурального числа, функция:
# def sumDidgits(n):
#     summa = 0              # накапливаем сумму с нуля
#     while n != 0:          # пока n не равно 0
#         summa += n % 10    # добавляем в summa последнюю цифру числа
#         n = n//10          # удаляем последнюю цифру числа
#     return summa
#
# n = int(input('Введиде число n: '))
# summa = sumDidgits(n)
# print(f'{n}, -> {summa}')
# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
# Пример:
# - 6782 -> 23
# - 0,56 -> 11
# cсумма цифр вещественного числа, функция: делал сам по аналогии примера, указанного выше
def sumrealNumberDidgits(n):
    summa = 0
    n = n * 1000000
    while n != 0:
        summa += n % 10
        n = n // 10
    return int(summa)
n = float(input('Введиде число n: '))
summa = sumrealNumberDidgits(n)
print(f'{n} -> {summa}')





