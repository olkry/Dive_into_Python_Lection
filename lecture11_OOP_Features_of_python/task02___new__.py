'''class User:

    def __init__(self, name: str):
        self.name = name
        print(f'Создал {self.name = }')

    def __new__(cls, *args, **kwargs):
        instance = super().__new__(cls)
        print(f'Создал класс {cls}')
        return instance


print('Создаём первый раз')
u_1 = User('Спенглер')
print('Создаём второй раз')
u_2 = User('Венкман')
print('Создаём третий раз')
u_3 = User(name='Стэнц')'''

# =======================================


'''class NamedInt(int):

    def __new__(cls, value, name):
        instance = super().__new__(cls, value)
        instance.name = name
        print(f'Создал класс {cls}')
        return instance


print('Создаём первый раз')
a = NamedInt(42, 'Главный ответ жизни, Вселенной и вообще')
print('Создаём второй раз')
b = NamedInt(73, 'Лучшее просто число')
print(f'{a = }\t{a.name = }\t{type(a) = }')
print(f'{b = }\t{b.name = }\t{type(b) = }')
c = a + b
print(f'{c = }\t{type(c) = }')'''


# ========================================

class Singleton:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self, name: str):
        self.name = name


a = Singleton('Первый')
print(f'{a.name = }')
b = Singleton('Второй')
print(f'{a is b = }')
print(f'{a.name = }\n{b.name = }')
