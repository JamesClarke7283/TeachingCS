""" Jargon

class:
    A blueprint for a thing that exists with more than one attribute.
    A Car can be represented as a class, a Person can too.

object:
    A object is the instance of a class, not the blueprint,
    but the expression of that idea.
    For example a Person called "Bob" is an object.
    As bob is an instance of the Person class.

instantiation:
    When you create an instance of a class.

self:
    A keyword to refer to the instance of this class.
    if there was a 'x' variable defined in the class, you would write 'self.x' to reference it.
    Same for methods, if there was a 'hello_world' method in the class,
    you would refer to 'self.hello_world()' to call it.

static method:
    Static means it does not depend on the class,
    therefor we don't need to parse self,
    its ISOLATED from the rest of the class

class method:
    Class methods are methods that are not dependent on the instance of the class,
    but on the class itself.

decorators:
    A decorator is a special attribute you can apply to a method to change its functionality.
    For example. you could add a custom decorator like so

class Person():

    @my_custom_log.info
    def get_name():
        return self.name

    @my_custom_log.info
    def get_age():
        return self.age

    The user gets the variable but also,
        this is Output in terminal:
        LOG: [INFO] 23/08/2022 : Bob
        LOG: [INFO] 24/08/2022 : 18
        LOG: [ERROR] 24/08/2022 : 18

dunder method / magic method:
    'dunder' means double underscore because it starts and ends with two underscores.

    A dunder method is a method which defines how the python interpreter should operate on the class, for example
    The person who made the int class defined the __add__ method to let Python know that the + symbol works on int objects.
"""


class Vehicle:
    def __init__(self, n_wheels, name):
        self.__n_wheels = n_wheels
        self.__name = name

    def get_n_wheels(self):
        return self.__n_wheels

    @staticmethod
    def static_method():
        """ Static means it does not depend on the class,
         therefor we don't need to parse self,
         its ISOLATED from the rest of the class """
        print("dddd")

    @classmethod
    def class_method(cls):
        """ Class methods are methods that are not dependent on the instance of the class,
            but on the class itself. """
        print("class method")
        cls.staticmethod()

    def get_name(self):
        return self.__name

    def set_n_wheels(self, n_wheels):
        self.__n_wheels = n_wheels

    def set_name(self, name):
        self.__name = name

    def __repr__(self) -> str:
        return f"Vehicle({self.__n_wheels}, {self.__name})"


# Vehicle.static_method()

"""
Inheritence, you can inherit from another class
"""


class Car(Vehicle):
    N_WHEELS = 4

    def __init__(self, name):
        super().__init__(self.N_WHEELS, name)
        
    def set_n_wheels(self, n_wheels):
        raise Exception("Number of wheels on a car needs to be 4")
    # set_n_wheels = property(doc='(!) Disallowed inherited: Car wheels need to be 4')


car = Vehicle(4, "Car")
print(car.set_n_wheels(3))
print(f"You have {car.get_n_wheels()} wheels on your Car, oops, better fix that")


nissan = Car("Nissan Leaf")
print(repr(nissan))
# nissan.set_n_wheels(3)
# print(nissan.get_n_wheels())
nissan.static_method()
nissan.name = "bob"
print(nissan.get_name())
