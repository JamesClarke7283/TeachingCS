# 4. Functions
# Functions are used to perform a specific task.

# TODO: Add section for pass by reference and pass by value

# Function definition
# Type hinting is optional, but recommended
def greeting(name: str) -> str:
    return "Hello " + str(name)


# Function call
name = "John"
print(greeting(name))
