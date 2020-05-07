from datetime import datetime
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # classmethod чтобы создать объект по году рождения,
    # "альтернативный" конструктор
    @classmethod
    def fromBirthYear(cls, name, year):
        return cls(name,  datetime.today().year - year)

    # статический метод,чтобы проверить совершеннолетие
    @staticmethod
    def isAdult(age):
        return age > 18

person1 = Person('Петя', 21)
person2 = Person.fromBirthYear('Петя', 1996)

print(person1.age)
print(person2.age)

# print the result
print(Person.isAdult(22))