# 3. Loops
# Loops are used to iterate over a sequence (list, tuple, string) or other iterable objects.

# For loop
# The for loop in Python is used to iterate over a sequence (list, tuple, string) or other iterable objects.
# i represents the current item in the sequence.
# you can name the variable anything you want.
for i in range(0, 5):
    print(i)

# Range Function
# The range() function returns a sequence of numbers,
# starting from 0 by default, and increments by 1 (by default), and ends at a specified number.
print(list(range(0, 5)))

# While loop
# With the while loop we can execute a set of statements as
# long as a condition is true.
i = 0
while i <= 5:
    print(i)
    i += 1
