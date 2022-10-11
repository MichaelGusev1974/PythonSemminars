 # Вычислить число c заданной точностью d
# Пример:
# - при d = 0.001, π = 3.141.;   10^{-1} ≤ d ≤10^{-10}
#from decimal import Decimal
# number = float(input('Введите число: '))
# d = int(input('количество знаков после запятой) для определения заданной точности числа: '))
#
# print(f'число  с заданной точностью {d} равно {round(number, d)}')
# 1
from decimal import Decimal                   # В конструктор передается строковое значение, которое представляет число:
# def accuracy(num, acc):
#     numder = Decimal(f'{num}')                  # Создаем объект Decimal со значением, которое д.б. строковым.
#     return numder.quantize(Decimal(f'{acc}'))      # quantize метод, который оставит acc знаков, после запятой т.е. 3 знака
# print(accuracy(float(input('Enter a real number: ')), float(input('Enter the required accuracy 0.0001: '))))
# 2
num = float(input('Enter a real number: '))
_, accu = input('Enter the required accuracy 0.0001: ').split('.')
print(f'{num:.{len(accu)}f}')