# a = 5
# print(a, id(a))
# a += 1
# print(a, id(a))

# Строка неизменяемый тип данных
# txt = 'Hello world!'
# txt[5] = '_'

# txt = 'Hello world!'
# print(txt, id(txt))
# txt = txt.replace(' ', '_')
# print(txt, id(txt))

a = d = 2
b = 3
print(a, id(a), b, id(b), d, id(d))
a = b + d
print(a, id(a), b, id(b), d, id(d))
