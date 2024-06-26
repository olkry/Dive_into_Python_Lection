from collections import namedtuple

Point = namedtuple('Point', 'x y z', defaults=[0, 0, 0])
a = Point(2, 3, 4)
b = a._replace(z=0, x=a.x + 4)
print(b)
data = [Point(2, 3, 4), Point(-10, -100, -500), Point(3, 7, 11), Point(2, 202, 1)]
print(data)
print(sorted(data))
# ==============================

d = {
    Point(2, 3, 4): 'first',
    Point(10, -100, -500): 'second',
    Point(3, 7, 11): 'last',
}
print(d)
mut_point = Point(2, [3, 4, 5], 6)
print(mut_point)
d.update({mut_point: 'bad_point'})  # TypeError: unhashable type: 'list'
