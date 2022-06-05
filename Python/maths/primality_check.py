import math
"""Checks if number is dividable by numbers other than 1 and itself.
:argument number_to_be_checked
:return Boolean whether is dividable by numbers other than 1 and itself
"""


def trial_division(num):
    for div_candidate in range(2, int(math.sqrt(num))):
        if num % div_candidate == 0:
            return 0
    else:
        return 1


"""Checks if number is a prime number
:argument number_to_be_checked
:return Boolean whether is prime or not
"""


def is_prime(num):
    # Checks if number is less than 2, or is an odd number greater than 2

    if num < 2 or (num % 2 == 0 and num > 2):
        return False

    # checks if is divisible by anything other than itself and 1
    elif trial_division(num) is 1:
        return True


lst = list(range(1, 1000))
for i in lst:
    result = "is a prime" if is_prime(i) else "is not a prime"
    print(i, result)
