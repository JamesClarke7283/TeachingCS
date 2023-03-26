import unittest
"""Unit testing is where you testware in components called units, you test each unit using a testing framework.
"""


def zebracase(string):
    new_str = list(string.lower())
    for index in range(len(string)):
        if index % 2 == 0:
            new_str[index] = string[index].upper()
    new_str = "".join(new_str)
    return new_str


class TestStringMethods(unittest.TestCase):
    def test_normal(self):
        self.assertEqual("TeSt", zebracase("test"))

    def test_fuzzy(self):
        self.assertEqual("TeStCaSe", zebracase("tESTcASE"))

    def test_extreme(self):
        self.assertEqual("PnEuMoNoUlTrAmIcRoScOpIcSiLiCoVoLcAnOcOnIoSiS", zebracase("pneumonoultramicroscopicsilicovolcanoconiosis"))
