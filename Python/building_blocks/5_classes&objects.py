""" There are 5 building blocks in Python:
    1. Variables
    2. Decisions
    3. Loops
    4. Functions
    5. Classes & Objects
"""


# 5. Classes & Objects
# Classes are used to create objects.


# Class definition
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greeting(self):
        print("Hello, my name is", self.name, "and I am", self.age, "years old")


# Object creation
person1 = Person("John", 36)