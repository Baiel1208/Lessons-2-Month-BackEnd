# 1) import random
# 2) from random import *
# 3) from random import randint

# Встроеные модули: random, time,datetime ,math, os
# Кастомный модули: person, calculator
#Внешные модули / библиотеки: 

# from person import Person
# import calculator

# from termcolor import colored ,cprint
# import datetime
# # current_date = datetime.datetime.now()
# print(current_date)
# cprint('Hello',color='red' ,on_color='on_blue' ,attrs=["bold", "underline"])


# p1 = Person("Esen")
# p1.say_my_name()

# s = calculator.addition(9,2)
# print(s)

from decouple import config
secret_key = config("SECRET_KEY", default="hahahahahah")
password = config("PASSWORD" ,cast=int)

print(secret_key)
print(password)