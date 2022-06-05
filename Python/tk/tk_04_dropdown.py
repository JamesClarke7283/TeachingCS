from tkinter import Tk, Label, Button, Listbox

import setuptools


class Vehicle:
    def __init__(self, name, max_speed, wheels=4):
        self.__name = name
        self.__wheels = wheels
        self.__max_speed = max_speed

    @property
    def name(self):
        return self.__name

    @property
    def wheels(self):
        return self.__wheels

    @property
    def max_speed(self):
        return self.__max_speed

class Plane(Vehicle):
    def __init__(self, name, max_speed, engines, wheels=4):
        self.__name = name
        self.__engines = engines
        self.__wheels = wheels
        self.__max_speed = max_speed

    @property
    def name(self):
        return self.__name

    @property
    def max_speed(self):
        return self.__max_speed

    @property
    def wheels(self):
        return self.__wheels

    @wheels.setter
    def wheels(self, num_wheels):
        match num_wheels:
            case num_wheels if num_wheels <= 3:
                raise ValueError(f"{num_wheels} is too few wheels")
            case num_wheels if num_wheels >= 10:
                raise ValueError(f"{num_wheels} is too many wheels")
            case _:
                self.wheels = num_wheels


class VehicleInfo:
    def __init__(self, vehicle_list):
        self.vehicle_list = vehicle_list
        self.window = Tk()
        self.window.title("Welcome to My app")
        self.window.geometry('350x200')
        self.lbl = Label(self.window, text="Hello")
        self.lbl.grid(column=0, row=0)
        self.txt = Listbox(self.window, width=10)
        self.txt.grid(column=1, row=0)
        for i in range(len(vehicle_list)):
            self.txt.insert(i+1, vehicle_list[i].name)
        btn = Button(self.window, text="Click Me", command=self.clicked)
        btn.grid(column=1, row=1)
        self.window.mainloop()

    def clicked(self):
        selected_v_str = self.txt.get(self.txt.curselection())
        vehicle_obj = None
        for i in range(len(vehicle_list)):
            if selected_v_str == vehicle_list[i].name:
                vehicle_obj = vehicle_list[i]
        self.lbl.configure(text=f"The vehicle has {vehicle_obj.wheels} wheels and {vehicle_obj.max_speed} km/h")
        print(selected_v_str)



A4 = Plane("A4", 250, 4, 5)
lambo = Vehicle("Lambo", 150, 4)
vehicle_list = []
vehicle_list.append(A4)
vehicle_list.append(lambo)

ve = VehicleInfo(vehicle_list)
