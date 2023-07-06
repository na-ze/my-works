"""
‘r’ - Открывает файл на чтение. (Значение по умолчанию)
'w’ - Открывает файл на запись. Если файла нет, то будет создан новый.
    Если файл существует, данные в нем будут перезаписаны.
'x’ - Открывает файл на запись. Если файл уже существует, операция завершится ошибкой.
'a’ - Открывает файл и дозаписывает в него данные, не стирая предыдущие.
    Создает новый файл, если он не существует.
't’ - Открывает файл как текстовый. (Значение по умолчанию)
'b’ - Открывает файл в бинарном/двоичном режиме.
'+' - Позволяет работать |: файлом как для записи так и для чтения.
"""
#ЧТЕНИЕ ФАЙЛА

#file = open(file="hello.txt", mode ="r", encoding='UTF-8')
#print(file.name)
#print(file.mode)
#print(file.read())
#file.close()

#with open(file="hello.txt") as file:
    #print(file.read()) #in read(кол-в символов)
    #print(file.readline) #считывает одну строку + делает ещё одну пустой
    #print(file.readlines) # считывает файл целиком, но построкам, делает список из строк

    #for line in file.readlines():
    #    print(line.strip())

    #for line in file:
        #print(line.strip())


#ЗАПИСЬ ФАЙЛА

#my_str = "Hack the Planet"
#passwords_list = ['qwerty', '12345', 'xxxxxx', 'I was here']
#
#with open(file="secret_file.txt",mode = "a") as file:
    #file.write(my_str)

    #for passwd in passwords_list:
        #file.write(f"{passwd}\n")



    #file.writelines([line + '\n' for line in passwords_list])

# РАБОТА С ИЗОБРАЖЕНИЯМИ

import requests

response = requests.get("https://img.championat.com/i/p/v/16224700311230977087.jpg")
with  open(file="cyberpunk.jpg", mode = "wb") as file:
    file.write(response.content)
