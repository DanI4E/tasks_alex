# import lesson_2


# def enter_name(name):
#     print(f"{name}, УРА!")
#     if name.count(' ') <= 1:
#         return name
    
# def ab(name):
#     name = name.strip().title()
#     return f"все гуууд {name}"
#     # print(type(name))
#     # print(name)


# print(enter_name(ab(input('Введите имя:'))))
# print(ab(input('Введите имя:')))



# def main():
#     while True:
#         en_name = input('Введите имя: ').strip()
#         if enter_name(en_name):
#             print('Ура')


# def enter_name(name):
#     if name.count(' ') <= 1 and len(name) >= 3:   
#         return name
#     else:
#         print('Некорректно введено имя')


# main()

# from functools import reduce
# import random

# def main():
#     random_number()


# def random_number():
#     m = random.randint(0,10)
#     while True:
#         enter_number = int(input('Проверь свою удачу. Введи число от 0 до 10: '))
#         if enter_number == m:
#             print(f"Успех, Загаданное цисло = {m}")
#             break
#         else:
#             print(f"Повезет в любви, Загаданное цисло = {m}")


# main()


# print(type(int(input('Проверь свою удачу. Введи число от 0 до 10: '))))

# m = list(reduce(random.randint(0,10), int(input('Проверь свою удачу. Введи число от 0 до 10: '))))
# print(m)


# d = reduce(lambda x,y: x+y,map(lambda x:x+x,filter(lambda x: (x>=3), int(input('Проверь свою удачу. Введи число от 0 до 10: ')))))
# print(d)
n = 0

# with open("auth22.txt", "r") as f:
#     print(f.readlines()[3])


# with open("C:/Python/Projects/lessons/lesson9/auth1.txt", "w") as f:
#     f.write('5\n')
#     f.write('5\n')
#     f.write('5\n')
#     f.write('5\n')
# print('e')




# m = open("C:/Python/Projects/lessons/lesson9/auth22.txt", "r")

# print(m.readlines())

# m.close()


# def _is_auth_file_exist():
#     try:
#         with open("C:/Python/Projects/lessons/lesson9/auth22.txt"):
#             return True
#     except Exception:
#         return False
    
# print(_is_auth_file_exist())


from authenticator import Authenticator

authenticator = Authenticator()

print(authenticator.__init__('admin', '1235'))
print(f'{authenticator.login}\n{authenticator._password}\n{authenticator.last_success_login_at}\n{authenticator.errors_count}')

a = input('Введите логин: ')
b = input('Введите пароль: ')
print(authenticator.authorize(a, b))


# print(authenticator.registrate(a, b))

# print(bool(authenticator.login))