from tkinter import *

window = Tk()

window.title("Welcome to My app")

window.geometry('350x200')

lbl = Label(window, text="Hello")

lbl.grid(column=0, row=0)


def clicked():
    lbl.configure(text="Clicked!!!")


btn = Button(window, text="Click Me", command=clicked)

btn.grid(column=0, row=1)

window.mainloop()
