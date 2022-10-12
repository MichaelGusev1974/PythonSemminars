#  В файле находится N натуральных чисел, записанных через пробел. Среди чисел не хватает одного, что бы выполнялось
#  условие A[i] -1 = A[i-1]. Найдите это число.
import random
import random
def get_array():
    path = 'C:/Users/Михаил/Desktop/Обучение в GeekBrains/Python/PythonSemminars/semminar5/n.txt'
    data = open(path, 'r')
    array = list(map(int, data.readline().split(' ')))
    data.close()
    print(array)
    array.remove(random.choice(array)) # сдесь рандомно удаляем один элемент из списка
    print(array)
    return array

def check_arr(array):
    if array[0] != 0:
        return 0
    for i in range(1, len(array)):
        if (array[i] - 1) != array[i - 1]:
            return i
    return -1

print(check_arr(get_array()))

