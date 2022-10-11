# Дан список чисел. Создайте список, в который попадают числа, описывающие возрастающую последовательность.
# Порядок элементов менять нельзя.
from random import choices
def get_list(size):
    return choices(range(size*2), k=size) # size*2 - диапазон, k=size - параметр к - количество эл-ов из диапазона
#print(get_list(10))     # вывод: [7, 9, 9, 6, 13, 17, 3, 16, 1, 4] случайные числа не по порядку

def new_list(array):
    new_list =[]
    for i in range(len(array)):
        some = array[i]
        arr = [some]
        for j in range(i + 1, len(array)):
             if array[j] > some:
                 arr.append(array[j])
                 some = array[j]
        if len(arr) > 2:
            new_list.append(arr)
    return new_list
d = get_list(10)
print(d, new_list(d), sep='\n')



