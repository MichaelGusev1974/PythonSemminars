# Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.
# вариант 2. :
def list_prime_factors(n):
    i = 2
    lst = []
    number = n
    while i <= n:
        if n % i == 0:
            lst.append(i)
            n //= i
            i = 2
        else:
            i += 1
    print(f"Простые множители числа {number} приведены в списке: {lst}")

n = int(input("Введите число: "))
list_prime_factors(n)