def my_func(data: list[int, float]) -> float:
    res = sum(data) / len(data)
    return res


print(sum([2, 5.5, 15, 8.0, 13.74]))
print(len([2, 5.5, 15, 8.0, 13.74]))
print(my_func([2, 5.5, 15, 8.0, 13.74]))

# можно и так

# def my_func(data):
#     res = sum(data) / len(data)
#     return res
#
#
# print(sum([2, 5.5, 15, 8.0, 13.74]))
# print(len([2, 5.5, 15, 8.0, 13.74]))
# print(my_func([2, 5.5, 15, 8.0, 13.74]))
