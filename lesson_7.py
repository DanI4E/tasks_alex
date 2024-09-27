import random

__author__ = "Danil Cherinov"

#  Принципы ООП (объектно ориентированного програмирования):
# Класс -  шаблон, описание объекта. 
# Объект - экземпляр класса, его реальное воплощение (car = Car())
# Метод класса - функция внутри класса.
# 1. Наследование - дочерние классы наследуют методы и свойства от родительского класса
# 2. Инкапсуляция - ограничения для использования методов, свойств, аргументов
# с помощью подчеркивания перед названием (_text - защищенная информация
# __text - очень защищенная информация). Используется внутри метода.
# 3. Полиморфизм - когда разные классы имеют одинаковые название методов или свойств 
# и которые можно вызвать в списке.
# 4. Абстракция - 
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



# Задачи:
# 1. int(age) нужно сделать после очистки строки от пробелов в конструкторе класса
# 2. в экземпляре класса создает переменную data_history, которая является пустым списком, 
# но будет хранить объекты класса Data — это вам необходимо знать для того, чтобы вы могли сделать type hint для этой переменной
# 3. Счетчик попыток оставить на месте как есть


class Data:
    def __init__(self, name: str, age: str):
        self.name = name
        self.age = age
        self.clear_whitespaces()
        self.age = int(age)

    def clear_whitespaces(self):
        self.name = self.name.strip()
        self.age = self.age.strip()


class Validator():
    def __init__(self):
        self.data_history: list[Data] = []

    def validate(self, data: Data):
        self.data_history.append(data)
        self.validate_name()
        self.validate_age()
    
    def validate_name(self):
        return self.data_history[0].name

    def validate_age(self):
        return self.data_history[0].age


def validate_name(name: str):
    """ Проверка имени на количество символов и что в имени есть только один пробел """

    if name.count(' ') <= 1 and len(name) >= 3:
        return
    
    raise Exception('Некорректно введено имя.') # заканчивается цикл
                             
                
def validate_age(age: int):
    """ Проверка возраста """

    if age <= 0 or age > 110:
        raise Exception("Дружочек, ты что-то не то ввел.")
    
    elif age <= 14:
        raise Exception(f"Твой возраст {age} сильно мал.")
    
    return


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

    while True:
        number += 1
        print(f"Попытка ввода данных №{number}.")
        enter_name = input('Введите имя: ')
        enter_age = input('Введите возраст: ')

        data = Data(enter_name, enter_age)

        validator = Validator()
        validator.validate(data)

        # try:
            # enter_age = int(clear_whitespaces(enter_age))
        # except ValueError:
            # print("Ошибка. Введите возраст цифрами")
            # continue
            
        try:
            validate_name(validator.validate_name())
        except Exception as e:
            print(f"Я cловил ошибку, {e}")
            continue

        try:
            validate_age(validator.validate_age())
        except Exception as e:
            print(f"Я cловил ошибку: {e}")
            continue
    
        print(get_passport_advice(validator.validate_age()))
        print(f"Привет {enter_name}, тебе {enter_age} лет. Ты ввел(а) корректные данные")
        guess_number_game()
        break

if __name__ == '__main__':
    main()