# 4. Functions
# Functions are used to perform a specific task.

# TODO: Add section for pass by reference and pass by value

# Function definition
# Type hinting is optional, but recommended
def greeting(name):
    return "Hello " + name


# Function call
name = "Mike"
output = greeting(name)
print(output)


# Function definition with multiple arguments
def add(num1, num2):
    return num1 + num2


num = add(5, 6)
print(num)


# Function definition with default arguments
def custom_greeting(name, greeting="Hello"):
    return greeting + " " + name


name = "Sam"
output = custom_greeting(name)
print(output)
