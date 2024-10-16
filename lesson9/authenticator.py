import json
import os
from typing import Optional
from exceptions import AuthorizationError, RegistrationError
from datetime import datetime



class Authenticator:
    def __init__(self):
        self.login: str | None = None
        self._password: Optional[str] = None
        self.last_success_login_at: Optional[datetime] = None
        self.errors_count: int = 0
        if self._is_auth_file_exist():
            self._read_auth_file()

    def _is_auth_file_exist(self) -> bool:
        """Проверка существует ли файл auth.json в корне проекта"""

        is_file_exist = os.path.exists("auth.json")
        if is_file_exist:
            return True

        return False

    def _read_auth_file(self):
        """Метод прочитывает файл и сохраняет строчки в переменные конструктора"""

        with open("auth.json") as f:
            reading_file = json.loads(f.read())

            self.login = reading_file['login']
            self._password = reading_file['password']
            self.last_success_login_at = reading_file['last_success_login_at'] # datetime.fromisoformat(f.readline().strip())
            self.errors_count = int(reading_file['errors_count'])

    def _update_auth_file(self):
        """Метод обновляет счетчик неудачных попыток авторизации и время авторизации"""

        with open("auth.json", "w") as f:
            data = {
                "login" : self.login,
                "password": self._password,
                "last_success_login_at" : self.last_success_login_at,
                "errors_count": self.errors_count
            }

            f.write(json.dumps(data))

    def authorize(self, login: str, password: str):
        """Метод авторизации. Сравнивает введенные логин и пароль с логином и паролем в файле auth.txt"""

        if self.login != login or self._password != password or self.login == None:
            self.errors_count += 1
            raise AuthorizationError("Логин и/или пароль не соответствуют")

        # для сериализации datetime в json надо объект datetime перевести в строку, перевожу с помощью strftime()
        self.last_success_login_at = datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S")
        self._update_auth_file()
        return "Вы авторизировались"

    def registrate(self, login: str, password: str):
        """Метод регистрации нового пользователя"""

        if self._is_auth_file_exist() or self.login is not None:
            self.errors_count += 1
            raise RegistrationError("Ошибка регистрации")


        self.login = login
        self._password = password
        self.last_success_login_at = datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S")
        self._update_auth_file()
