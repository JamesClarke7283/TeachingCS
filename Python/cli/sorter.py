import sys

numbers = sys.argv[1::]

def check_list_type(lst):
    dictionary = {}
    for item in lst:
        try:
            dictionary[type(item)] += 1
        except KeyError:
            dictionary[type(item)] = 1
    return dictionary

new_numbers = []  

# Convert the list of strings to a list of integers
try:
    for number in numbers:
        new_numbers.append(int(number))
except ValueError:
    if check_list_type(numbers)[type(str())] == 1:
        numbers = numbers[0].split(",")
        for number in numbers:
            new_numbers.append(int(number))

# Sort the list of integers
for item in sorted(new_numbers):
    print(item, end=' ')
print()

