"""Double inheritance
Here is an example of double inheritance. The SubClass inherits from both
ParentClass1 and ParentClass2.
"""


class ParentClass1:
    def __init__(self):
        print("ParentClass1's __init__")


class ParentClass2:
    def __init__(self):
        print("ParentClass2's __init__")


class SubClass(ParentClass1, ParentClass2):
    def method3(self):
        super(ParentClass1, self).__init__()  # Calls ParentClass1's method1
        super(ParentClass2, self).__init__()  # Calls ParentClass2's method2


def main():
    """Main function"""
    sub = SubClass()
    sub.method3()


if __name__ == "__main__":
    main()
