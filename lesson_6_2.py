"""Lesson 6"""

# Исключения - блочная конструкция try, exception, 
# else - выводим только безошибочные результаты.
# finaly - всегда выводим блок
# 
# 
# Так же есть конструкция raise Exception() - где мы можем описать ошибку.
# 
# 
# 
# try:
    # a = int(input("Enter"))
# exceprion:
    # print("Всё окк")




# Homework 6
# 1. Оптимизировать алгоритм. +
# 2. Переименовать функции. +
# 3. Все функции валидации ('validate_name', 'validate_age') должны всегда возвращать 'None', а в случае ошибки -
# делать raise Exception(текст ошибки). +
# 4. Использовать функцию 'clear_whitespaces' еще и для введенной строки, в которой должно быть число. +
# 5. В функции "main", необходимо отловить ошибки и функции 'validate_name', 'validate_age'. Вывести пользователю:
# 'Я поймал ошибку: {текст ошибки}'. И если ошибки были, тогда вам необходимо заново запросить у пользователя ввод данных.
# 6. В функции 'main' обрабатывать ошибку ValueError (не использкем Exception) во время перевода строки к int. +
# 7. Перед запросом данных в функции 'main' пользователю должно печататься номер текущей попытки ввода данных. Пользователю отображать попытки
# начиная с 1, а в коде должно быть с 0. +
# 8. Во время игры 'Угадай число' тоже должен быть счетчик попыток, который будет указываться при успешно угаданному числу. + 

import random

def clear_whitespaces(name):
# Удаление пробелов сначала и сконца значения
    return name.strip()


def validate_name(name: str) -> str:
# Проверка имени на количество символов и что в имени есть только один пробел
    if name.count(' ') <= 1 and len(name) >= 3:
        return
    raise Exception('Некорректно введено имя.') # заканчивается цикл
                             
                
def validate_age(age: int) -> str:
# Проверка возраста
    if age <= 0 or age > 110:
        raise Exception("Дружочек, ты что-то не то ввел.")
    elif age <= 14:
        raise Exception(f"Твой возраст {age} сильно мал.")
    return


def get_passport_advice(age: int) -> str:
# Рекомендации по замене паспорта
    if 16 <= age <= 17:
        return f"Твой возраст {age}. Не забудь получить первый паспорт."
    elif 25 <= age <= 26:
        return f"Твой возраст {age}. Нужно заменить паспорт."
    elif 45 <= age <= 46:
        return f"Твой возраст {age}. Нужно заменить паспорт 2-ой раз."
    else:
        return "Нет необходимости менять паспорт"


def guess_number_game():
# Игра угадай число от 1 до 5
    n = 0
    m = random.randint(0,5)
    while True:
        n += 1
        enter_number = int(input('Проверь свою удачу. Введи число от 0 до 5: '))
        if enter_number == m:
            print(f"Успех, Загаданное цисло = {m}. Отгадано с {n} попыток")
            break
        print(f"Повезет в любви, Загаданное цисло = {m}")


def main():
# Выполнения функций ввода имени, ввода возраста и других функций
    number = 0
    while True:
        number += 1
        print(f"Попытка ввода данных №{number}.")
        enter_name = input('Введите имя: ')
        enter_age = input('Введите возраст: ')

        enter_name = clear_whitespaces(enter_name)

        try:
            enter_age = int(clear_whitespaces(enter_age))
        except ValueError:
            print("Ошибка. Введите возраст цифрами")
            continue
            
        try:
            validate_name(enter_name)
        except Exception as e:
            print(f"Я cловил ошибку, {e}")
            continue

        try:
            validate_age(enter_age)
        except Exception as e:
            print(f"Я cловил ошибку: {e}")
            continue
    
        print(get_passport_advice(enter_age))
        print(f"Привет {enter_name}, тебе {enter_age} лет. Ты ввел(а) корректные данные")
        guess_number_game()
        break


main()