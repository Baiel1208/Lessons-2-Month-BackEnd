# ДЗ №1
# 1. Создать класс Person с атрибутами fullname, age, is_married

class Person:
    def __init__(self, fullname, age, is_married):
        self.fullname = fullname 
        self.age = age
        self.is_married = is_married


# 2. Добавить в класс Person метод introduce_myself, который бы распечатывал всю информацию о человеке


    def introduce_myself(self):
        print(f"Full name: {self.fullname}. age: {self.age}. ")
        if self.is_married:
            print("Married.")
        else:
            print("Single.")

person1 = Person("Артур Мартур", 50, is_married=True)
person1.introduce_myself() 


# 3. Создать класс Student наследовать его от класса Person и дополнить его атрибутом marks, который был бы словарем, где ключ это название урока, а значение - оценка.

class Student(Person):
    def __init__(self, fullname, age, is_married, marks):
        super().__init__(fullname, age, is_married)
        self.marks = marks

    def average_mark(self, ):
        return sum(self.marks.values()) / len(self.marks) # МЕТОД 4 - ЗАДАНИИ
    
student = Student(fullname="Joe Tomas", age=19, is_married="Single", marks={"math": 90, "history": 80, "biology": 95})
print(f"Fullname: {student.fullname}. Age: {student.age}. Is_married: {student.is_married}. Marks: {student.marks}")


# 4. Добавить метод в класс Student, который бы подсчитывал среднюю оценку ученика по всем предметам

student1_marks = {"math": 90, "history": 80, "biology": 95}
student1 = Student("Joe Tomas", 19, False, student1_marks)
print(student1.average_mark()) 


# 5. Создать класс Teacher и наследовать его от класса Person, дополнить атрибутом experience.

class Teacher(Person):
    def __init__(self, fullname, age, is_married, experience, salary):
        super().__init__(fullname, age, is_married)
        self.experience = experience
        self.salary = salary  # ЗАДАНИЯ 6

    def calculate_salary(self):
        standard_salary = self.salary
        if self.experience > 3:
            bonus = 0.05 * (self.experience - 3 ) * standard_salary
            return standard_salary + bonus  
        else:
            return standard_salary

teacher1 = Teacher("Mary John", 35, True, 10 , 30000)
print(f"Fullname: {teacher1.fullname}. Age: {teacher1.age}. Is_married: {teacher1.is_married}. Experience: {teacher1.experience}. Salary: {teacher1.salary}")


# 6. Добавить в класс Teacher атрибут уровня класса salary """^|^"""

# 7. Также добавить метод в класс Teacher, который бы считал зарплату по следующей формуле: к стандартной зарплате прибавляется бонус 5% за каждый год опыта свыше 3х лет.

print( teacher1.calculate_salary()) 

# 8. Создать объект учителя и распечатать всю информацию о нем и высчитать зарплату

"""Вроде выходит информация об учителе"""

# 9. Написать функцию create_students, в которой создается 3 объекта ученика, эти ученики добавляются в список и список возвращается функцией как результат.

def create_student():
    student1 = Student("Joe Tomas", 19, False, {"math": 90, "history": 80, "biology": 95} )
    student2 = Student("Joe Biden", 18, False, {"math": 50, "history": 40, "biology": 45})
    student3 = Student("Joe Tom", 20, False, {"math": 20, "history": 60, "biology": 55})

    students = [student1, student2, student3]
    return students


# students_list = create_student()
# print(students_list)



# 10. Вызвать функцию create_students и через цикл распечатать всю информацию о каждом ученике с его оценками по каждому предмету. Также рассчитать его среднюю оценку по всем предметам

students_list = create_student()

for studentss in students_list:
    studentss.introduce_myself()
print("Average grade:", studentss.average_mark())

