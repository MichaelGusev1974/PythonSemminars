# Пример проверки ложности утверждения:
# (X ≡ Z) V (X → (Y ∧ Z))
# состояний возможно только два 1 и 0, True и False # print(x) вывод: 0, 1
# for x in range(2):
#     for y in range(2):
#         for z in range(2):
#           print(x, y, z)   # вывод: все состояния трех переменных:
# 0 0 0
# 0 0 1
# 0 1 0
# 0 1 1
# 1 0 0
# 1 0 1
# 1 1 0
# 1 1 1
for x in range(2):
    for y in range(2):
        for z in range(2):
            if  not (x == z or x <= y and z):
                print(x, y, z)
# проверкa ложности утверждения: (X ≡ Z) V (X → (Y ∧ Z)) вывод:
# 1 0 0
# 1 1 0



#  в if мы можем попасть только по истине (x == z or x <= y and z): вывод:
# 0 0 0
# 0 0 1
# 0 1 0
# 0 1 1
# 1 0 1
# 1 1 1
