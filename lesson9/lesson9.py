from authenticator import Authenticator
import random
# from exceptions import ValidateError


__author__ = "Danil Cherinov"

def guess_number_game():
    """ Игра угадай число от 1 до 5 """

    n = 0
    m = random.randint(0,5)

    while True:
        n += 1
        enter_number = int(input('Проверь свою удачу. Введи число от 0 до 5: '))

        if enter_number == m:
            print(f"Успех, Загаданное цисло = {m}. Отгадано с {n} попыток. Игра создана {__author__}")
            break

        print(f"Повезет в любви, Загаданное цисло = {m}")


def main():
    """ Выполнения функций ввода имени, ввода возраста и других функций """

    authenticator = Authenticator()

    if authenticator.login:
        text = 'Для авторизации необходимо ввести логин и пароль'
    else:
        text = 'Необходимо пройти регистрацию'

    print(text)


    # counter = 0
    # last_attempt = 0

    while True:
        # counter += 1
        login = input('Введите логин: ')
        password = input('Введите пароль: ')

        if text == 'Необходимо пройти регистрацию':
            authenticator.registrate(login, password)
        else:
            authenticator.authorize(login, password)


        # last_attempt = counter
        # if counter == last_attempt:
        #     data_with_date = DataWithDate()
        #     last_attempt = data_with_date.time

        print(f"Привет {login.title()}")
            #   f"Первая попытка ввода данных была в {first_attempt.strftime('%H:%M:%S')}. "
            #   f"Ты ввел(а) корректные данные c №{counter} попытки в {last_attempt.strftime('%H:%M:%S')}.\n"
            #   f"Разница времени между первой и последней попыткой ввода данных: {time_difference.seconds//3600}:{(time_difference.seconds//60)%60}:{time_difference.seconds//1}")
        guess_number_game()
        break

if __name__ == '__main__':
    main()