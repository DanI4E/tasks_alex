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
        """Проверка существует ли файл auth.txt в корне проекта"""

        is_file_exist = os.path.exists("auth.txt")
        if is_file_exist:
            return True

        return False

    def _read_auth_file(self):
        """Метод прочитывает файл и сохраняет строчки в переменные конструктора"""

        with open("auth.txt", "r") as f:
            self.login = f.readline().strip()
            self._password = f.readline().strip()
            self.last_success_login_at = f.readline().strip()
            self.errors_count = int(f.readline().strip())

    def _update_auth_file(self):
        """Метод обновляет счетчик неудачных попыток авторизации и время авторизации"""

        with open("auth.txt", "w") as f:
            f.write(self.login + '\n')
            f.write(self._password + '\n')
            f.write(self.last_success_login_at + '\n')
            f.write(str(self.errors_count))

    def authorize(self, login: str, password: str):
        """Метод авторизации. Сравнивает введенные логин и пароль с логином и паролем в файле auth.txt"""

        if self.login != login or self._password != password or self.login == None:
            self.errors_count += 1
            raise AuthorizationError("Логин и/или пароль не соответствуют")

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
