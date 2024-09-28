from datetime import datetime
from exceptions import ValidationError

class Data:
    def __init__(self, name: str, age: str):
        self.name = name
        self.age = age
        self._clear_whitespaces()
        self.age = int(age)

    def _clear_whitespaces(self):
        self.name = self.name.strip()
        self.age = self.age.strip()

class DataWithDate(Data):
    def __init__(self):
        return datetime.now().strftime('%H:%M:%S')

class Validator:
    def __init__(self):
        self.data_history: list[Data] = []
    
    def _validate_name(self):
        """ Проверка имени на количество символов и что в имени есть только один пробел """

        name = self.data_history[-1].name

        if name.count(' ') <= 1 and len(name) >= 3:
            return name
        
        raise ValidationError('Некорректно введено имя.') # заканчивается цикл

    def _validate_age(self):
        """ Проверка возраста """

        age = self.data_history[-1].age

        if age <= 0 or age > 110:
            raise ValidationError("Дружочек, ты что-то не то ввел.")
    
        elif age <= 14:
            raise ValidationError(f"Твой возраст {age} сильно мал.")
    
        return age
    
    def _validate_null(self):
        """Проверка на пустоту"""

        if not self.data_history:
           raise ValueError("Проверка на пустоту data_history") 

    
    def validate(self, data: Data):
        self.data_history.append(data)
        self._validate_name()
        self._validate_age()
