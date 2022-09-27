# Задайте список из N элементов, заполненных числами из промежутка [-N, N].
# Найдите произведение элементов на указанных позициях. Позиции хранятся в файле file.txt в одной строке одно число.
n = int(input('Задайте список числа n: '))
position_one = int(input('Позиция1: '))
position_two = int(input('Позиция2: '))
listing = []
for i in range(-n, n + 1):
    listing.append(i)
print(listing)
print(listing[position_one - 1] * listing[position_two - 1])
