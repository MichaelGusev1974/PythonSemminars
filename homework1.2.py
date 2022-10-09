# Напишите программу для. проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.
# Идеальное решение - гуглил!!!
# for x in range(2):
#         for y in range(2):
#             for z in range(2):
#                 print(not (x or y or z) == (not x and not y and not z))
#                 print(x, y, z)

for x in range(2):
        for y in range(2):
            for z in range(2):
                if not (x or y or z) == (not x and not y and not z):
                    print(x, y, z)


# x = int(input('Введите число x '))
# y = int(input('Введите число y '))
# z = int(input('Введите число z '))
#
# leftSide = not (x or y or z)
# rightSide = not x and not y and not z
# result = leftSide == rightSide
#
# if result == True:
#     print('Утверждение истинно')
# else:
#     print('Утверждение ложно')
