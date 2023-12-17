import sys

# x = int("42")
# y = int(3.1415)
# z = int("hello", base=30)
# print(x, y, z, sep='\n')
#
# print('-------------------------------')
#
# STEP = 2 ** 16
# num = 1
# for _ in range(30):
#     print(sys.getsizeof(num), num)
#     num *= STEP
#
# # print(STEP)
# print(num, type(num))
#
# print('-------------------------------')

num = 2 ** 16 - 1
b = bin(num)
o = oct(num)
h = hex(num)
print(b, o, h, sep='\n')
