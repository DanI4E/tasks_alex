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
# n = 0

# with open("C:/Python/Projects/lessons/lesson9/fauth.txt", "r") as f:
#     for i in f.readlines():
#         if i == 3:
#             n = f.readline()

    
    
#     print(n)


# with open("C:/Python/Projects/lessons/lesson9/auth1.txt", "w") as f:
#     f.write('5\n')
#     f.write('5\n')
#     f.write('5\n')
#     f.write('5\n')
# print('e')




# m = open("C:/Python/Projects/lessons/lesson9/auth.txt", "r")

# print(m.readlines())

# m.close()


# def _is_auth_file_exist():
#     try:
#         with open("C:/Python/Projects/lessons/lesson9/auth.txt"):
#             return True
#     except Exception:
#         return False
    
# print(_is_auth_file_exist())

from authenticator import Authenticator
import random
from exceptions import ValidateError


authenticator = Authenticator()

print(bool(authenticator.login))