""" Make a TODO application

1. People need a numbered list of current todos,
name

2. Ability to add TODOs, ability to remove TODOs.

3. Ability to exit.
"""


arr = ["A", "B", "C"]

r = range(len(arr))

print("Indexes", list(r))
print("Values", arr)

z = zip(range(len(arr)), arr)
print("Using Zip:", list(z))
print("Enumerate:", list(enumerate(arr)))

"""
for index, value in zip(range(len(arr)), arr):
    print(index + 1, value)
"""

# Make version of above statement using enumerate
