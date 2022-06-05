# regular functions
# lambda/anonymous functions

def foo(*args, end=" "):
    if args != list():
        for i in args:
            print(i, end=end)
        return args
    else:
        raise Exception("You need at least 1 argument")


foo(end="|")


def print_hi(first_name, last_name):
    print(str.format("\nHello, {} {}.", first_name, last_name))


print_hi(last_name="Bob", first_name="Marley")


# class
# object


class Vehicle:
    def __init__(self, n_wheels, name):
        self.__n_wheels = n_wheels
        self.__name = name

    def get_n_wheels(self):
        return self.__n_wheels

    @staticmethod
    def static_method():
        print("dddd")
        pass

    def get_name(self):
        return self.__name

    def set_n_wheels(self, n_wheels):
        self.__n_wheels = n_wheels

    def set_name(self, name):
        self.__name = name


class Car(Vehicle):
    def __init__(self, name):
        self.__n_wheels = 4
        self.__name = name


class Person:
    def __init__(self, age, name, lengt):
        self.__age = age
        self.__name = name
        self.__length = lengt


class VIP(Person):
    def __init__(self, age, name, length):
        self.__age = age
        self.__name = name
        self.__length = length
        self.is_important = True


c = Vehicle(4, "Tesla")

c.set_name("BMW")
print(c.get_n_wheels())

n = Car("Nissan")
print(n.get_n_wheels())

array = [1, 2, 3]

# Collection

# Dictionary
d = {"name": "bob", "age": 10}
f = {"names": "sara", "age": 12}

g = []
g.append(d)
g.append(f)

for i in g:
    print(i["name"])

print(g)


name = ""