text = input('Введите любые символы: ')
if text.isdigit():
    print('Число ', text, 'в двоичной системе: ', bin(int(text)), '\n',
          'В восьмеричной системе: ', oct(int(text)), '\n',
          'В шестнадцатеричной системе; ', hex(int(text)))
else:
    if text.isascii():
        print('Текст', text, 'записан в кодировке ASCII')
    else:
        print('Текст', text, 'записан не в кодировке ASCII')
