class Vehicle:
    MIN_WHEELS = 1
    MAX_WHEELS = 10

    def __init__(self, n_wheels, name):
        self.__n_wheels = n_wheels
        self.__name = name

    @property
    def n_wheels(self):
        return self.__n_wheels

    @property
    def name(self):
        return self.__name

    @n_wheels.setter
    def n_wheels(self, n_wheels):
        match n_wheels:
            case n_wheels if n_wheels < self.MIN_WHEELS:
                raise ValueError(f"Cannot have less than {self.MIN_WHEELS} wheel")
            case n_wheels if n_wheels > self.MAX_WHEELS:
                raise ValueError(f"You Cannot have vehicles with {self.MAX_WHEELS} or more wheels")
            case _:
                self.__n_wheels = n_wheels

    @name.setter
    def name(self, name):
        self.__name = name


c = Vehicle(4, "Car")
c.n_wheels = 1
print(c.n_wheels)