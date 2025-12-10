from random import randint

system_int = randint(1,100)

while True:
    user_int = int(input('Введите число: '))

    if user_int < system_int:
        print('Ваше число меньше того, что загадано')

    if user_int > system_int:
        print('Ваше число больше того, что загадано')

    if user_int == system_int:
        break

print('Отличная интуиция! Вы угадали число :)')
