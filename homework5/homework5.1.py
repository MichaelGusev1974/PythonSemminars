# Напишите программу, удаляющую из текста все слова, содержащие ""абв"".
# my_list = list(' Напишитеабв программу, удаляющуюабв из текста все слова, содержащие ""абв'.split())
# 1 Вариант
# for i in my_list:
#     if 'абв' not in i:
#         print(i, end='  ')

# 2 вариант
# print(list(filter(lambda i: 'абв' not in i, my_list)))

# 3 вариант
# print([i for i in my_list if 'абв' not in i])

# 4 вариант
from random import sample
def list_rand_words(count: int, alp: str = 'абв'): # ф-я формирующая строку, параметры: количество и строка (любая)
    word_list = []
    for i in range(count):                       # в цикле крутимся указанное кол-во раз (count)
        letters = sample(alp, 3)                 # метод sample выдаст выборку по (3)символа , без дубликатов, случайным образом.
        word_list.append("".join(letters))       # добавляем в список склееные сиволы join-ом в элементы
    return "".join(word_list)                    # возвращаем список из слов


# def list_rand_words(count: int, alp = 'абв'):
#   renurn "".join("".join(sample(alp, 3) for _ in range(count))  - то же, только в строку!

def simple_sentence(words: str) -> str:
    return "".join(words.replace("абв", "").split())




