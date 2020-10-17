# class methods without instances

# *************
# classmethod
# *************
# A class method receives the class as implicit first argument, just like an instance method receives the instance
# - A class method is a method which is bound to the class and not the object of the class.
# - They have the access to the state of the class as it takes a class parameter that points to the class
# and not the object instance.
# - It can modify a class state that would apply across all the instances of the class.
# For example it can modify a class variable that will be applicable to all the instances.

class File:
    # class attribute
    folder = "/home/boo"

    @classmethod
    def change_folder(cls, new_folder_name):
        cls.folder = new_folder_name


file1 = File()
print(file1.folder)
file1.change_folder("/new_folder")  # or File.change_folder(...)
print(file1.folder)  # folder attribute changed for all instances


# *************
# staticmethod
# *************
# A static method does not receive an implicit first argument.
# - A static method is also a method which is bound to the class and not the object of the class.
# - A static method can’t access or modify class state.
# - It is present in a class because it makes sense for the method to be present in class.
import datetime


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # a class method to create a Person object by birth year.
    @classmethod
    def from_birth_year(cls, name, year):
        return cls(name, datetime.date.today().year - year)

    # a static method to check if a Person is adult or not.
    @staticmethod
    def is_adult(age):
        return age > 18


person1 = Person('mayank', 21)
person2 = Person.from_birth_year('mayank', 1996)

print(person1.age)
print(person2.age)

# staticmethod called
print(Person.is_adult(22))
