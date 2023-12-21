my_list = ['H', 'e', 'l', 'l', 'o', 1, 7, 5, 3]
my_list.sort()  # TypeError: '<' not supported between instances of 'int' and 'str'
res = sorted(my_list)  # TypeError: '<' not supported between instances of 'int' and 'str'
print(my_list)
print(res)
