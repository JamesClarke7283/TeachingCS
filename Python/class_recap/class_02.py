def acceptable(value):
    if 100 >= value >= 0:
        return True
    return False


class Protective:
    def __init__(self):
        self._protected_value = 0

    @property
    def protected_value(self):
        return self._protected_value

    @protected_value.setter
    def protected_value(self, value):
        if acceptable(value):
            self._protected_value = value
        else:
            raise ValueError("Value needs to range between 0 and 100")


p = Protective()
p.protected_value = 100
print(p.protected_value)
