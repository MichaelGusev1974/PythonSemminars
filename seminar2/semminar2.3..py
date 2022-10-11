# Напишите программу, в которой пользователь будет задавать две строки, а программа - определять количество вхождений
# одной строки в другую.

# a = input('Введите строку 1: ')
# b = input('Введите строку 2: ')

# print(a.count(b))               # лучший вариант при помощи метода count

# Альтернативный вариант:
# if len(a) < len(b):
#     a, b = b, a                    # замена переменной ( не нужна третья как в С#)
# count = 0
# for i in a:
#     for j in b:
#         if i == j:
#             count += 1
# print(count)

print('gipopotampo'.count('po')) # сколоко вхождений подстроки 'ро' в строку 'gipopotamo' метод count
# вывод 3
print('gipopotampo'.count('po', 3)) # второй параметр - индекс, с какого считать кол-во вхождений
# вывод 2
print('gipopotampo'.count('po', 3, 7)) # диапазон индексов эл-ов строки, между которыми считаем кол-во вхождений в строку
# вывод 1
# методы - это специальный вид функций, написанный под определенный тип данных
# типы данных - это классы, а функции в классах - это методы.
# У строк, списков, кортежей - методы схожие, это семейства, где поддерживается индексация слайзы и т.п.

print('1 2 3'.split(' ')) # вывод: ['1,', '2,', '3']

print('1           2 3'.split(' ')) # вывод:['1,', '', '', '', '', '', '', '', '', '', '', '2,', '3']
print('1           2 3'.split()) # из метода split() убрали пробелы и: ['1,', '2,', '3']
print('1 2 3'.split(','))                   # вывод:['1 2 3'] убрали запятые

print(" ".join(["Name", "Surname"])) # объединит эл-ты списка в строку: 'Name Surname'
print(" - ".join(["Name", "Surname"])) # вывод: 'Name - Surname'
print('gipopotampo'.replace('po', 'pa')) # gipapatampa - замена подстрок
# все методы строк не меняют исходную строку, создается новый объект и его куда-то надо сохранять, если с ним нужно работать