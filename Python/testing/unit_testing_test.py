import unittest

class StringMethods:
    @staticmethod
    def zebracase(string):
        new_str = list(string.lower())
        for index in range(len(string)):
            if index % 2 == 0:
                new_str[index] = string[index].upper()
        new_str = "".join(new_str)
        return new_str


class TestStringMethods(unittest.TestCase):
    def test_normal(self):
        self.assertEqual("TeSt", StringMethods.zebracase("test"))
    
    def test_fuzzy(self):
        self.assertEqual("TeStCaSe", StringMethods.zebracase("tESTcASE"))
    
    def test_extreme(self):
        self.assertEqual("PnEuMoNoUlTrAmIcRoScOpIcSiLiCoVoLcAnOcOnIoSiS", StringMethods.zebracase("pneumonoultramicroscopicsilicovolcanoconiosis"))
