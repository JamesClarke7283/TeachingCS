""" In python a generator is a function that 
returns an object (iterator) which we can iterate over 
(one value at a time). """

def simple_generator():
    yield 1
    yield 2
    yield 3

for value in simple_generator():
    print(value)

print()

# Example of a generator that yields a sequence of numbers
def count_up_to(max):
    count = 1
    while count <= max:
        yield count
        count += 1

counter = count_up_to(5)
for i in counter:
    print(i)

print()

def count_down_to(min, initial_value = 10):
    count = initial_value
    while count >= min:
        yield count
        count -= 1

counter = count_down_to(5, 10)
for i in counter:
    print(i)