# Дан список, вывести отдельно буквы и цифры
# 1
inp_string = list(map(str, input('Введите строку с буквами и числами: ').split()))
result_digits = [i for i in inp_string if i.isdigit()]
result_letters = [i for i in inp_string if not i.isdigit()]
print(result_digits, '\n', result_letters)

# 2
# a = ( "a", 'b', '2', '3' ,'c')
# b = ( 'a' , 'b' , 'c')
# c = ( '1', '2', '3')
#
#
# b= filter(str.isalpha, a)
# c= filter(str.isdigit, a)
#
# print(*b)
# print(*c)