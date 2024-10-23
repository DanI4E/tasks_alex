import json
import os
from typing import Optional
from exceptions import AuthorizationError, RegistrationError
from datetime import datetime
from validator import Validator



class Authenticator:
    def __init__(self):
        self.email: str | None = None
        self._password: Optional[str] = None
        self.last_success_login_at: Optional[datetime] = None
        self.errors_count: int = 0
        if self._is_auth_file_exist():
            self._read_auth_file()

    @staticmethod
    def _is_auth_file_exist() -> bool:
        """Проверка существует ли файл auth.json в корне проекта"""

        return os.path.exists("auth.json")

    def _read_auth_file(self):
        """Метод прочитывает файл и сохраняет строчки в переменные конструктора"""

        with open("auth.json") as f:
            reading_file = json.loads(f.read())

            self.email = reading_file['email']
            self._password = reading_file['password']
            self.last_success_login_at = datetime.fromisoformat(reading_file['last_success_login_at']) # datetime.fromisoformat(f.readline().strip())
            self.errors_count = int(reading_file['errors_count'])

    def _update_auth_file(self):
        """Метод обновляет счетчик неудачных попыток авторизации и время авторизации"""

        with open("auth.json", "w") as f:
            data = {
                "email" : self.email,
                "password": self._password,
                # для сериализации datetime в json надо объект datetime перевести в iso формат, перевожу с помощью isoformat()
                "last_success_login_at" : self.last_success_login_at.isoformat(),
                "errors_count": self.errors_count
            }

            f.write(json.dumps(data))


    def authorize(self, email: str, password: str):
        """Метод авторизации. Сравнивает введенные логин и пароль с логином и паролем в файле auth.txt"""

        with open("auth.json") as f:
            if self.email != email or Validator().validate_password(password) != json.loads(f.read())['password'] or self.email is None:
                self.errors_count += 1
                raise AuthorizationError("Email и/или password не соответствуют.")


        self.last_success_login_at = datetime.utcnow()
        self._update_auth_file()
        return "Вы авторизировались."

    def registrate(self, email: str, password: str):
        """Метод регистрации нового пользователя"""

        if self._is_auth_file_exist() or self.email is not None:
            self.errors_count += 1
            raise RegistrationError("ошибка регистрации.")


        self.email = email
        self._password = password
        self.last_success_login_at = datetime.utcnow()
        self._update_auth_file()