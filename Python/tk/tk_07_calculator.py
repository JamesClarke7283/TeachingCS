from tkinter import *

window = Tk()

window.title("Calculator App")

calc_frame = Frame(window)
calc_frame.pack(side="top")

result_lbl = Label(calc_frame, text="Test", background="white")
result_lbl.pack(side="top")

number_pad = Frame(calc_frame)
number_pad.pack(side="bottom")

btn_0 = Button(number_pad, text="0")
btn_0.grid(column=1, row=1)


window.mainloop()