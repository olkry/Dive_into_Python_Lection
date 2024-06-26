import time
from collections import namedtuple
from datetime import datetime

PAUSE = 3

User = namedtuple('User', ['first_name', 'last_name', 'birthday'], defaults=['Иванов', datetime.now()])
u_1 = User('Исаак')
print(f'{u_1.last_name}, {u_1.birthday.strftime("%H:%M:%S")}')
print(f'Пауза в {PAUSE} секунд.')
time.sleep(PAUSE)
u_2 = User('Галилей', 'Галилео')
print(f'{u_2.last_name}, {u_2.birthday.strftime("%H:%M:%S")}')
