name = 'Alex'
age = 12
text = f'Меня зовут {name} и мне {age} лет'
print(text)

print(f'{{Фигурные скобки}} и {{name}}')

pi = 3.1415
print(f'Число Пи с точностью два знака: {pi:.2f}')

data = [3254, 4364314532, 43465474, 2342, 462256, 1747]
for item in data:
    print(f'{item:>10}')

num = 2 * pi * data[1]
print(num)
print(f'{num = :_}')  # выводим имя переменной, знак равенства с пробелами до и после него и только потом значение.
                      # число разделяется символом подчёркивания для деления на блоки по 3 цифры.



