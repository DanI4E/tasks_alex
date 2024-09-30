from exceptions import AuthorizationError, RegistrationError
from datetime import datetime


class Authenticator:
    """Аутентификация пользователя"""

    def __init__(self, login: str | None = None, _password: str | None = None, last_success_login_at: datetime | None = None, errors_count: int = 0):
        self.login = login
        self._password = _password
        self.last_success_login_at = last_success_login_at
        self.errors_count = errors_count

    
    def _is_auth_file_exist(self):
        try:
            with open("C:/Python/Projects/lessons/lesson9/auth.txt"):
                return True
        except Exception:
            return False


    def _read_auth_file(self):
        with open("C:/Python/Projects/lessons/lesson9/auth.txt", "r") as f:
            self.login = f.readline().strip()
            self._password = f.readline().strip()
            self.last_success_login_at = f.readline().strip()
            self.errors_count = f.readline().strip()


    def authorize(self, login: str, password: str):
        if self.login == login and self._password == password:
            return self.login, self._password
        
        if self.login == None:
            raise AuthorizationError("Логина нет")
        
        self.errors_count += 1
        self._update_auth_file()
        raise AuthorizationError("Логин и/или пароль не соответствуют")


    def _update_auth_file(self):
        with open("C:/Python/Projects/lessons/lesson9/auth.txt", "w") as f:
            f.write(self.login + '\n')
            f.write(self._password + '\n')
            f.write(self.last_success_login_at + '\n')
            f.write(self.errors_count)


    def registrate(self, login: str, password: str):
        if self._is_auth_file_exist():
            raise RegistrationError("Файл auth.txt рядом")
        
        if self.login is not None:
            raise RegistrationError("login не None")
        
        with open("C:/Python/Projects/lessons/lesson9/auth.txt", "a") as f:
            f.write(login + '\n')
            f.write(password + '\n')
            f.write(datetime.utcnow().isoformat() + '\n')
            f.write(self.errors_count)



        
            

    




    