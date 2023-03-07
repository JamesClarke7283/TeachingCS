from enum import IntEnum

"""Enumerations
    - Enumerations are a set of symbolic names (members) bound to unique, constant values.
    - The members can be compared by identity, and the enumeration itself can be iterated over.
    - Enumerations can be used to represent a fixed set of constant values, such as the days of the week, months in a year, or suits in a deck of cards. 
"""


class Colour(IntEnum):
    """Colour enumeration
    """
    RED = 1
    GREEN = 2
    BLUE = 3


# funtional syntax for enums
colour = IntEnum('Color', ['RED', 'GREEN', 'BLUE'])

# print the enum
print(Colour.RED)

# print the enum value
print(Colour.RED.value)
