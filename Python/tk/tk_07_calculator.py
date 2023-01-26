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
btn_0.grid(column=1, row=4)

btn_1 = Button(number_pad, text="1")
btn_1.grid(column=1, row=2)

btn_2 = Button(number_pad, text="2")
btn_2.grid(column=2, row=2)

btn_3 = Button(number_pad, text="3")
btn_3.grid(column=3, row=2)

btn_4 = Button(number_pad, text="4")
btn_4.grid(column=1, row=1)

btn_5 = Button(number_pad, text="5")
btn_5.grid(column=2, row=1)

btn_6 = Button(number_pad, text="6")
btn_6.grid(column=3, row=1)

btn_7 = Button(number_pad, text="7")
btn_7.grid(column=1, row=0)

btn_8 = Button(number_pad, text="8")
btn_8.grid(column=2, row=0)

btn_9 = Button(number_pad, text="9")
btn_9.grid(column=3, row=0)

window.mainloop()