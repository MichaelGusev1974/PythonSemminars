#  Преобразовать набора списков
# users = ['user1','user2','user3','user4','user5']
# ids = [4, 5, 9, 14, 7]
# salary = [111,222,333]
# в другой набор
#
# ['user1', 4, 111]
# ['user2', 5, 222]
# ['user3', 9, 333]
#
# и потом вернуть в исходное состояние
#
# ['user1', 'user2', 'user3']
# [4, 5, 9]
# [111, 222, 333]
# 1 вариант
# users = ['user1', 'user2', 'user3', 'user4', 'user5']
# ids = [4, 5, 9, 14, 7]
# salary = [111, 222, 333]
# result = list(zip(users,  ids,  salary))
# print(result)
#
# new_users = [i[0] for i in result]
# new_ids = [i[1] for i in result]
# new_salary = [i[2] for i in result]
# print(new_users, '\n', new_ids, '\n', new_salary)

# 2 вариант
users = ['user1', 'user2', 'user3', 'user4', 'user5']
ids = [4, 5, 9, 14, 7]
salary = [111, 222, 333]

a, b, c = map(list, zip(users, ids, salary))
print(a, b, c, sep="\n")
a, b, c= map(list, zip(a, b, c))

print(a, b, c, sep="\n")