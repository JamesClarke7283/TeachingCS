import unittest

# Author: darkmatt3r00


class ShoppingList:
    def __init__(self):
        self.items = []

    def add(self, item):
        self.items.append(item)

    def remove(self, item):
        for i, v in enumerate(self.items):
            if v == item:
                del self.items[i]

    def list(self):
        for i, v in enumerate(self.items):
            print(i + 1, v)


class TestShoppingList(unittest.TestCase):
    def test_add(self):
        sl = ShoppingList()
        sl.add('Bread')
        self.assertEqual(['Bread'], sl.items)

    def test_remove(self):
        sl2 = ShoppingList()
        sl2.list()
        sl2.add('Bread')
        sl2.add('Eggs')
        sl2.remove('Eggs')
        self.assertEqual(['Bread'], sl2.items)
