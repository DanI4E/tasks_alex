import random
from exceptions import ValidationError
from validator import Validator, Data#, DataWithDate


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
# 1. int(age) нужно сделать после очистки строки от пробелов в конструкторе класса
# 2. в экземпляре класса создает переменную data_history, которая является пустым списком, 
# но будет хранить объекты класса Data — это вам необходимо знать для того, чтобы вы могли сделать type hint для этой переменной
# 3. Счетчик попыток оставить на месте как есть


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


def main():
    """ Выполнения функций ввода имени, ввода возраста и других функций """

    number = 0
    validate = Validator()

    while True:
        number += 1
        enter_name = input('Введите имя: ')
        enter_age = input('Введите возраст: ')

        data = Data(enter_name, enter_age)

        validate.validate(data)

        print(validate._validate_name(), validate._validate_age())

        # try:
            # enter_age = int(clear_whitespaces(enter_age))
        # except ValueError:
            # print("Ошибка. Введите возраст цифрами")
            # continue
            
        try:
            validate._validate_null()
            validate._validate_name()
            validate._validate_age()
        except ValidationError as e:
            print(f"Я cловил ошибку : {e}")
            print(f"Попытка ввода данных №{number}.")
            continue

        # data_with_date = DataWithDate()
# 
        # print(data_with_date)


        print(get_passport_advice(validate._validate_age()))
        print(f"Привет {enter_name}, тебе {enter_age} лет. Ты ввел(а) корректные данные c №{number} попытки.")
        guess_number_game()
        break

if __name__ == '__main__':
    main()