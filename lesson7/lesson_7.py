"""Lesson 7"""

import random
from exceptions import ValidateError
from datetime import datetime
from validator import Validator, Data, DataWithDate


__author__ = "Danil Cherinov"

#  Принципы ООП (объектно ориентированного програмирования):
# Класс -  шаблон, описание объекта. (self - экземпляр класса)
# Объект - экземпляр класса, его реальное воплощение (car = Car())
# Метод класса - функция внутри класса.
# __init__, __gt__, __ge__ и тд. - магические методы (__init__ - конструктор класса)
# 1. Наследование - дочерние классы наследуют методы и свойства от родительского класса
# 2. Инкапсуляция - ограничения для использования методов, свойств, аргументов
# с помощью подчеркивания перед названием (_text - защищенная информация
# __text - очень защищенная информация). Используется внутри метода.
# 3. Полиморфизм - когда разные классы имеют одинаковые название методов или свойств 
# и которые можно вызвать в списке.
# 4. Абстракция - ###
# 
# 
# 
# 
# 
# 
# 
# Работа с git
# 1. Git - система управления версиями (основная ветка - main, далее делаем развлетвление branch,)
#  Основные команды git
#  git init - инициализация репозитория
#  git status - статус репозитория
#  git add *название файла - добавление файла в репозиторий
#  git commit -m *текст коммита - коммит файла, папки с описанием того что сделали
#  git diff *название файла- посмотреть изменение кода
#  git branch *название ветки - создание ветки
#  git switch *название ветки - перейти в созданную ветку
#  git push origin * название ветки - запушить в github
#  git branch -m * new-name -  изменение названия ветки
#  git rm * название файла - удаление файла
#  git merge * название ветки какую буду мержить - надо находится в target ветке
#  git pull origin master - спулить обновление с удаленной master ветки на локальную master ветку


# Задачи:
# 1. Исправить все нюансы, которые были озвучены во время проверки домашки на последнем уроке.
# 2. Создать модуль exceptions, в нем класс ValidationError, который наследуется от Exception. 
#    Никакие методы, свойства переопределять не нужно, необходимо только описать в docstring, что это класс ошибки валидации данных
# 3. Создать модуль validator, в котором:
#     3.1. Реализовать класс Data, конструктор которого принимает name и age аргументы, сохраняет их в одноименные переменные экземпляра класса. 
#           Так же у этого класса должен быть метод _clear_whitespaces, который очищает от пробелов в начале и в конце переменные name и age у экземпляра класса. 
#           Вызывать метод _clear_whitespaces необходимо из конструктора класса.
#     3.2. Реализовать класс DataWithDate, наследовавшись от класса Data. 
#           Конструктор должен делать то же самое, что и родительский класс, но дополнительно сохраняет текущее время, когда был создан этот экземпляр класса ( см. datetime.utcnow).
#     3.3. Реализовать класс Validator. У класса Validator должны быть следующие методы:
#         а. конструктор класса — в экземпляре класса создает переменную data_history, которая является пустым списком, но будет хранить объекты класса Data.
#         b. _validate_name — валидация имени (скопировать код из функции validate_name).
#         c. _validate_age — валидация возраста (скопировать код из функции validate_age).
#         d. validate — принимает аргумент data (объект класса Data) и сохраняет в список data_history. Далее запускает методы валидации, описанные выше.
#     При этом методы _validate_name и _validate_age должны брать имя и возраст из переменной Validator.data_history (самое последнее значение). 
#     А также выбрасывать исключения ValidationError вместо Exception. Если переменная data_history пуста, тогда выбрасывать исключение ValueError.
# 4. В вашем основном файле, где вся текущая домашка:
#     4.1. В самом верху необходимо импортировать класс Validator из модуля validator.

#     4.2. В самом верху необходимо импортировать класс ValidationError из модуля exceptions.
#     4.3. В функции main до цикла создать объект класса. Вызвать метод validate вместо тех функций валидаций, которые были написаны в домашках ранее - эти функции необходимо удалить из этого файла. 
#           Обрабатывать ошибку ValidationError вместо Exception.
#     4.4. После того как пользователь ввел данные, необходимо создать объект класса DataWithDate и далее работать только с ним.
#     4.5. Теперь количество попыток ввода данных должно выводиться только в том случае, если пользователь не смог с первого раза ввести верные данные.
#     4.6. После ввода верных данных и до запуска игры необходимо показать пользователю:
#         a. Общее количество попыток
#         b. Время первой попытки, время последней попытки
#         c. Сколько времени понадобилось пользователю, чтобы от первой попытки дойти к последней (формат HH:MM:SS, где HH - часы, MM - минуты, SS - секунды)


def get_passport_advice(age: int) -> str:
    """ Рекомендации по замене паспорта """

    if 16 <= age <= 17:
        return f"Твой возраст {age}. Не забудь получить первый паспорт."
    
    elif 25 <= age <= 26:
        return f"Твой возраст {age}. Нужно заменить паспорт."
    
    elif 45 <= age <= 46:
        return f"Твой возраст {age}. Нужно заменить паспорт 2-ой раз."
    
    else:
        return "Нет необходимости менять паспорт"


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


def format_timedelta(td):
    """ Перевод значения timedelta к format(hours, minutes, seconds)"""

    minutes, seconds = divmod(td.seconds + td.days * 86400, 60)
    hours, minutes = divmod(minutes, 60)
    return '{:d}:{:02d}:{:02d}'.format(hours, minutes, seconds)


def main():
    """ Выполнения функций ввода имени, ввода возраста и других функций """

    counter = 0
    first_attempt = datetime.utcnow()
    validate = Validator()

    while True:
        counter += 1
        enter_name = input('Введите имя: ')
        enter_age = input('Введите возраст: ')

        data = DataWithDate(enter_name, enter_age)

        if counter == 1:
            first_attempt = data.time

        try:
            validate.validate(data)

        except ValidateError as e:
            print(f"Я cловил ошибку : {e}\nПопытка ввода данных №{counter}.")
            continue

        time_difference = data.time - first_attempt

        print(get_passport_advice(data.age), f"\nПривет {enter_name.title()}, тебе {enter_age} лет. " 
              f"Первая попытка ввода данных была в {first_attempt.strftime('%H:%M:%S')}. "
              f"Ты ввел(а) корректные данные c №{counter} попытки в {data.time.strftime('%H:%M:%S')}.\n"
              f"Разница времени между первой и последней попыткой ввода данных: {format_timedelta(time_difference)}")
        
        break

    guess_number_game()

if __name__ == '__main__':
    main()