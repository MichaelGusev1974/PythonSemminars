# Напишите программу, удаляющую из текста все слова, содержащие ""абв"".
my_list = list(' Напишитеабв программу, удаляющуюабв из текста все слова, содержащие ""абв'.split())
# 1
# for i in my_list:
#     if 'абв' not in i:
#         print(i, end='  ')
# 2
print(list(filter(lambda i: 'абв' not in i, my_list)))
# 3
print([i for i in my_list if 'абв' not in i])
