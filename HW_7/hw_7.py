# ДЗ №6
# 1. Создать класс под названием data, в класс добавить атрибуты full_name, email, file_name, color. 
# Добавить геттеры и сеттеры для всех атрибутов
import re

class Data:
    def __init__(self,full_name,email,file_name,color) -> None:
        self.__full_name = full_name
        self.__email = email
        self.__file_name = file_name
        self.__color = color
# full_name
    @property
    def full_name(self):
        return self.__full_name
    
    @full_name.setter
    def full_name(self, value):
        self.__full_name = value
# email
    @property
    def email(self):
        return self.__email
    
    @email.setter
    def email(self, value):
        self.__email = value
# file_name
    @property
    def file_name(self):
        return self.__file_name
    
    @file_name.setter
    def file_name(self, value):
        self.__file_name = value
# color
    @property
    def color(self):
        return self.__color
    
    @color.setter
    def color(self, value):
        self.__color = value

# 2. Затем считать из файла MOCK_DATA.txt, в котором 1000 строк с данными (Имя и Фамилия, почта, название файла с расширением и код цвета)
# 3. Из каждой считанной строки создать объект класса data и добавить его в список.


with open('MOCK_DATA.txt', 'r',encoding='utf-8') as file:
    list = file.readlines()
    print(list)

    with open('full_name.txt','w+'):
        full_name = re.findall(r"^[A-Za-z-]+\s[A-Za-z-' \.]+", list)
        for a in full_name:
            print(a)

    with open('email.txt', 'w+') as email:
        email = re.findall(r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b", list)
        for i in email:
            print(i)


    with open('file_name.txt','w+') as file_name:
        file_name = re.findall(r"\.[^.]*$\b", list)
        for b in file_name:
            print(b)
    
    with open('color.txt','w+') as color:
        color = re.findall(r"#([A-Fa-f0-9]{6})", list)
        for c in color:
            print(c)
