"""
МОДУЛЬ 3
 В проекте создать новый модуль 3seq.py. Задание:

Пользователь вводит элементы 1-го списка (по очереди как в МОДУЛЬ 1 или вместе как в МОДУЛЬ 2)
Затем он вводит элементы 2-го списка
Удалить из первого списка элементы присутствующие во 2-ом и вывести результат на экран

Пример работы: Введите элементы 1-го списка: 1,2,3,4,5
Введите элементы 2-го списка: 2,5
Результат: 1,3,4

Предлагаю проверить работу программы на разных списках, чтобы убедиться что она работает верно
"""
str1 = input("Введите элементы 1-го списка через запятую:")
if str1.find(",")==-1:
    if str1.find(";")==-1:
        str12 = str1.split("/")
    else:
        str12 = str1.split(";")
else:
    str12 = str1.split(",")
str2 = input("Введите элементы 2-го списка через запятую:")
if str2.find(",")==-1:
    if str2.find(";")==-1:
        str22 = str2.split("/")
    else:
        str22 = str2.split(";")
else:
    str22 = str2.split(",")
str3 = []
for i in str12:
    if not(i in str22):
        str3.append(i)
for i in str3:
    print(i, end=' ')