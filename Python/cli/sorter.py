import sys

numbers = sys.argv[1::]

# Convert the list of strings to a list of integers
new_numbers = []
for number in numbers:
    new_numbers.append(int(number))

# Sort the list of integers
for item in sorted(new_numbers):
    print(item, end=' ')
