a = b = c = 0
a += 42
print(f'{a=} {b=} {c=}')


a = b = c = {1, 2, 3}
a.add(42)
print(f'{a=} {b=} {c=}')


a, b, c = 1, 2, 3
print(f'{a=} {b=} {c=}')


t = 1, 2, 3
print(f'{t=}, {type(t)}')