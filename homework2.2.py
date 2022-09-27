#Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.
# Пример: - пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)

n = int(input('Введиде число n: '))
i = 1
number = 1
listing = []
while i <= n:
    number = number*i
    listing.append(number)
    i += 1
print(listing)



