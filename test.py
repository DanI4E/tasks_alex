def auth_or_reg(func):
    print('auth_or_reg')
    def wrapper():
        while True:
            result = func().upper()
            if result:
                print(result)
                break
    return wrapper


@ auth_or_reg
def main():
    print('Вызвана функция')
    login = input("Введите логин: ").strip(" ")
    password = input("Введите пароль: ").strip(" ")
    return f"{login}, {password}"

main()



