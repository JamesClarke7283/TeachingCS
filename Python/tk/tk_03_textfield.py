from tkinter import Tk, Label, Entry, Button

window = Tk()

window.title("Welcome to My app")

window.geometry('350x200')

lbl = Label(window, text="Hello")

lbl.grid(column=0, row=0)

txt = Entry(window, width=10)

txt.grid(column=1, row=0)


def clicked():
    lbl.configure(text="Button was clicked !!")
    input_txt = txt.get()
    print(input_txt)


btn = Button(window, text="Click Me", command=clicked)

btn.grid(column=1, row=1)

window.mainloop()