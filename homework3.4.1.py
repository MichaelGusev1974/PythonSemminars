# Напишите программу, которая будет преобразовывать десятичное число в двоичное.
# Пример: - 45 -> 101101; - 3 -> 11; - 2 -> 10
# 2 способ:
# number = int(input('Введите число: '))
# result = []
# while number > 0:
#     result.append(number % 2)
#     number //= 2
# result_revers = result[::-1]                # cпособ нарезки
# print(result_revers)
#
# number = int(input('Введите число: '))
# print(bin(number))                          # метод bin() для проверки правильности вывода

# 3 способ:

def conv_bin(num: int):
    list_nums = []
    while num > 0:
        list_nums.insert(0, num % 2)
        num //= 2

    print(list_nums)
    print(*list_nums)
    print(*list_nums, sep='')

conv_bin(int(input('Ввод чмсла: ')))
