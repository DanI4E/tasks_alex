"""Lesson 11"""

from authenticator import Authenticator
from validator import Validator
import random
# import datetime
# import time

__author__ = "Danil Cherinov"


# Задачи:
# 1. В файл сохранять теперь данные в формате json
#
# 2. Разобраться как сериализовать datetime в json (Гугл, а потом написать подробно в комменте почему именно так)
#
# 3. *Написать класс валидатора, написать валидацию для пароля: минимум 4 символа, минимум один заглавный символ,
# минимум один прописной символ, минимум одна цифра, минимум один спецсимвол. Хэшировать пароль любым алгоритмом
# на выбор, обосновать в комменте выбор алгоритма (можно хоть свой сделать). Написать метод валидации почты.
# Вместо логина у вас должен быть ввод почтового адреса.


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


# def format_timedelta(td):
#     """ Перевод значения timedelta к format(hours, minutes, seconds)"""
#
#     minutes, seconds = divmod(td.seconds + td.days * 86400, 60) # divmod выводит частное и остаток
#     hours, minutes = minutes // 60, minutes % 60
#     return '{:d}:{:02d}:{:02d}'.format(hours, minutes, seconds)


def format_timedelta(td):
    """ Перевод значения timedelta к format(hours, minutes, seconds)"""
    return td.seconds // 60

def auth_or_reg(func):
    """Декоратор принимает функцию func(), выходит из декоратора при достижении функции значения True"""

    def wrapper():
        while not func():
            pass
    return wrapper


@auth_or_reg
def main():
    """ Выполнения функций ввода имени, ввода возраста и других функций """


    authenticator = Authenticator()
    validate = Validator()

    if authenticator.email:
        text = 'Для авторизации необходимо ввести email и пароль'
    else:
        text = 'Необходимо пройти регистрацию'

    print(text)

    email = input('Введите email: ').strip()
    password = input('Введите пароль: ').strip()

    if text == 'Необходимо пройти регистрацию':
        try:
            validate_email = validate.validate_email(email)
            validate_password = validate.validate_password(password)
            authenticator.registrate(validate_email, validate_password)
            print("Вы зарегистрировались!")

        except Exception as e:
            print(f"Еще раз, {e}")
            return None
    else:
        try:
            if authenticator.authorize(email, password):
                print(f"Привет {email}! Последняя успешная авторизация в "
                      f"{authenticator.last_success_login_at.strftime('%d-%m-%Y %H:%M:%S')}."
                      f"\nВы пытались {authenticator.errors_count} раз войти в приложение с ошибкой авторизации.")


        except Exception as e:
            print(f"Еще раз, {e}")
            return None

    guess_number_game()

    return True


if __name__ == '__main__':
    main()
    # time.sleep(60)
    # print(f"Время последней авторизации: {authenticator.last_success_login_at.strftime('%d-%m-%Y %H:%M:%S')}\n")
    # delta_minute = datetime.datetime.utcnow() - authenticator.last_success_login_at
    # print(f"Кол-во минут разницы между текущем временем и последней авторизацией: {format_timedelta(delta_minute)} минут")

