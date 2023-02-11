# Globals and functions

def greeting(name):
    print("Hello", name)


# Global Variables
GREET = "Hello"


def greeting2(name):
    global GREET
    print(GREET, name)


greeting("James")
