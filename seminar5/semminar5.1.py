# НОД двух чисел
def find_simple(n):
    list_n = []
    for i in range(1,n):
        if n % i == 0:
            list_n.append(i)
            n / i
    return list_n

x = 24
y = 54
list_x = find_simple(x)
list_y = find_simple(y)

print(list_x)
print(list_y)

esult=list(set(list_x) & set(list_y))
print(max(esult))
