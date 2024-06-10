# class User:
#
#     def __init__(self, name):
#         self._name = name
#
#     @property
#     def name(self):
#         return self._name
#
#
# user = User('Стивен')
# print(f'{user.name = }')
# user.name = 'Славик'  # AttributeError: can't set attribute 'name'

# ======================================================================

class User:

    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    @property
    def full_name(self):
        return f'{self.first_name} {self.last_name}'


user = User('Стивен', 'Спилберг')
print(f'{user.first_name = }\n{user.last_name = }\n{user.full_name = }')
# user.full_name = 'Стивен Хокинг'  # AttributeError: can't set attribute 'full_name'
user.last_name = 'Хокинг'
print(f'{user.first_name = }\n{user.last_name = }\n{user.full_name = }')
