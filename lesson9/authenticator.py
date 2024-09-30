from datetime import datetime

class Authenticator:
    """Аутентификация пользователя"""

    def __init__(self, login: str | None = None, _password: str | None = None, last_success_login_at: str = None, datetime: datetime = None, errors_count: int = 0):
        self.login = login
        self._password = _password
        self.last_success_login_at = last_success_login_at
        self.datetime = datetime
        self.errors_count = errors_count

    
    def _is_auth_file_exist():
        with open("C:\Python\Projects\lessons\lesson9\auth.txt", "r") as f:
            print(f.readlines())
            return

    def _read_auth_file():
        pass
    




    