tupl = ('one', 42), ('two', 3.14), ('ten', 'Hello world!')
print(type(tupl))
a = {'one': 42, 'two': 3.14, 'ten': 'Hello world!'}
b = dict(one=42, two=3.14, ten='Hello world!')
c = dict([('one', 42), ('two', 3.14), ('ten', 'Hello world!')])
d = dict(tupl)
print(type(d))
print(a == b == c == d)

print(d)
print(d.keys())
print(d.values())
print(d['ten'])
