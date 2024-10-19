import re
import hashlib
from exceptions import RegistrationError, AuthorizationError

class Validator:
    def __init__(self):
        self.email: str
        self.password: str


    def validate_password(self, password: str) -> None | str:
        """Проверка на создание пароля и хеширование пароля"""

        if re.search(r'(?=.*\d)(?=.*[a-z])(?=.*[A-Z])(?=.*\W).{4,}', password):
            result = hashlib.sha256(password.encode())
            return result.hexdigest()
        raise RegistrationError("Пароль должен содержать минимум 4 символа:\n"
                                "Минимум одна заглавная английская буква, минимум одна прописная английская буква,\n"
                                "минимум одна цифра, минимум один специальный символ.")


    def validate_email(self, email: str):
        """Проверка на создание email"""

        if re.search(r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$', email):
            return email
        raise RegistrationError("Email введен неверно")
