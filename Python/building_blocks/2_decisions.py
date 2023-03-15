# 2. Decisions
# Decisions are used to make decisions based on conditions.
my_int = 5

# If statement
if my_int == 5:
    print("my_int is equal to 5")

# If-else statement
if my_int == 5:
    print("my_int is equal to 5")
else:
    print("my_int is not equal to 5")

# If-elif-else statement
if my_int == 5:
    print("my_int is equal to 5")
elif my_int == 6:
    print("my_int is equal to 6")
else:
    print("my_int is not equal to 5 or 6")

# Match statement
# You can use match statement in Python 3.10
match my_int:
    case 5:
        print("my_int is equal to 5")
    case 6:
        print("my_int is equal to 6")
    case _:
        print("my_int is not equal to 5 or 6")
