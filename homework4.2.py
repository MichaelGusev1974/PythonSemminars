# Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.
# вариант 1. :
def prim_factors(n):
   i = 2
   listing = []
   while i * i <= n:
       while n % i == 0:
           listing.append(i)
           n = n // i
       i = i + 1
   if n >= 1:
    listing.append(n)
    return listing
n = int(input('Введите число: '))
print(prim_factors(n))


