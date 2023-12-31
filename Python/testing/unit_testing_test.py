import unittest
"""Unit testing is where you test software in components called units, you test each unit using a testing framework.
"""


def zebracase(string):
    new_str = list(string.lower())
    for index in range(len(string)):
        if index % 2 == 0:
            new_str[index] = string[index].upper()
    new_str = "".join(new_str)
    return new_str


def reversecase(string):
    input_str = string[::-1]
    return input_str


def startend_upper(string):
    string = list(string.lower())
    string[0] = string[0].upper()
    string[-1] = string[-1].upper()
    return ''.join(string)


class TestStringMethods(unittest.TestCase):
    def test_normal(self):
        self.assertEqual("TeSt", zebracase("test"))

    def test_fuzzy(self):
        self.assertEqual("TeStCaSe", zebracase("tESTcASE"))

    def test_extreme(self):
        self.assertEqual("PnEuMoNoUlTrAmIcRoScOpIcSiLiCoVoLcAnOcOnIoSiS", zebracase("pneumonoultramicroscopicsilicovolcanoconiosis"))


class TestReverseCase(unittest.TestCase):
    def test_normal(self):
        self.assertEqual("What", reversecase("tahW"))

class TestStartEndUpper(unittest.TestCase):
    def test_normal(self):
        self.assertEqual("PizzA", startend_upper("pizza"))