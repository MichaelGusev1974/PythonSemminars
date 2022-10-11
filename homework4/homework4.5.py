#Даны два файла, в каждом из которых находится запись многочлена. Задача - сформировать файл, содержащий сумму многочленов.
# 1 способ
# with open('file_hw44.txt', 'r') as file_hw44:
#     data_first = file_hw44.read()
# if len(data_first) > 20:
#     a, b, c = int(data_first[0]), int(data_first[9]), int(data_first[18])
#     print(a, b, c)
# elif len(data_first) > 8:
#     a, b, c = int(data_first[0]), int(data_first[9]), 0
#     print(a, b, c)
# else:
#     a, b, c = int(data_first[0]), 0, 0
# with open('file_hw45.txt', 'r') as file_hw45:
#     data_second = file_hw45.read()
# if len(data_second) > 20:
#     a1, b1, c1 = int(data_second[0]) + a, int(data_second[9]) + b, int(data_second[18]) + c
#     print(a1, b1, c1)
# elif len(data_second) > 8:
#     a1, b1, c1 = int(data_second[0]) + a, int(data_second[9]), 0 + c
#     print(a1, b1, c1)
# else:
#     a1, b1, c1 = int(data_second[0]) + a, 0 + b, 0 + c
# result = ''
# k = 2
# if b1 == 0: result = f'{a1}*x**{k} + {c1}*x**{k-2} = 0'
# if b1 == 0 and c1 == 0: result = f'{a1}*x**{k} = 0'
# if c1 == 0: result = f'{a1}*x**{k} + {b1}*x**{k-1} = 0'
# else: result = f'{a1}*x**{k} + {b1}*x**{k-1} + {c1}*x**{k-2} = 0'
# with open('file_sum.txt', 'w') as file_sum:
#     file_sum.write(f'({data_first} + {data_second}) = {result}')
# print(f'({data_first} + {data_second}) = {result}')

# 2 способ

def poly_sum(name_1: str, name_2: str):
    with open(name_1, 'r', encoding='utf-8') as m_f_1, \
            open(name_2, 'r', encoding='utf-8') as m_f_2:
        first = m_f_1.readlines()
        second = m_f_2.readlines()
        if len(first) == len(second):
            with open('sum_poly.txt', 'a', encoding='utf-8') as m_f_3:
                for i, v in enumerate(first):
                    m_f_3.write(f"{v[:-5]} + {second[i]}")
        else:
            print('The contents of the files do not match')

poly_sum('poly.txt', 'poly_2.txt')


