from tkinter import *
from enum import IntEnum


class Operation(IntEnum):
    ADD = 0
    SUB = 1
    MUL = 2
    DIV = 3


window = Tk()

window.title("Calculator App")

calc_frame = Frame(window)
calc_frame.pack(side="top")

result_lbl = Label(calc_frame, text="", background="white")
result_lbl.pack(side="top")

number_pad = Frame(calc_frame)
number_pad.pack(side="bottom")

accumulator = 0
op = Operation

def btn_0_clicked():
    current_text = result_lbl['text']
    result_lbl.config(text=current_text+"0")


def btn_1_clicked():
    current_text = result_lbl['text']
    result_lbl.config(text=current_text+"1")


def btn_2_clicked():
    current_text = result_lbl['text']
    result_lbl.config(text=current_text+"2")


def btn_3_clicked():
    current_text = result_lbl['text']
    result_lbl.config(text=current_text+"3")


def btn_4_clicked():
    current_text = result_lbl['text']
    result_lbl.config(text=current_text+"4")


def btn_5_clicked():
    current_text = result_lbl['text']
    result_lbl.config(text=current_text+"5")


def btn_6_clicked():
    current_text = result_lbl['text']
    result_lbl.config(text=current_text+"6")


def btn_7_clicked():
    current_text = result_lbl['text']
    result_lbl.config(text=current_text+"7")


def btn_8_clicked():
    current_text = result_lbl['text']
    result_lbl.config(text=current_text+"8")


def btn_9_clicked():
    current_text = result_lbl['text']
    result_lbl.config(text=current_text+"9")


def btn_add_clicked():
    global accumulator
    global op
    accumulator = int(result_lbl['text'])
    result_lbl.config(text="")
    op = Operation.ADD


def btn_sub_clicked():
    global accumulator
    global op
    accumulator = int(result_lbl['text'])
    result_lbl.config(text="")
    op = Operation.SUB


def btn_mul_clicked():
    global accumulator
    global op
    accumulator = int(result_lbl['text'])
    result_lbl.config(text="")
    op = Operation.MUL


def btn_div_clicked():
    global accumulator
    global op
    accumulator = int(result_lbl['text'])
    result_lbl.config(text="")
    op = Operation.DIV


def btn_clear_clicked():
    result_lbl.config(text="")
    pass


def btn_calc_clicked():
    global op
    global accumulator
    second_accumulator = int(result_lbl['text'])
    result = 0
    match op:
        case Operation.ADD:
            result = accumulator + second_accumulator
        case Operation.SUB:
            result = accumulator - second_accumulator
        case Operation.MUL:
            result = accumulator * second_accumulator
        case Operation.DIV:
            result = accumulator / second_accumulator
    result_lbl.config(text=str(result))


btn_0 = Button(number_pad, text="0", command=btn_0_clicked)
btn_0.grid(column=1, row=3)

btn_1 = Button(number_pad, text="1", command=btn_1_clicked)
btn_1.grid(column=1, row=2)

btn_2 = Button(number_pad, text="2", command=btn_2_clicked)
btn_2.grid(column=2, row=2)

btn_3 = Button(number_pad, text="3", command=btn_3_clicked)
btn_3.grid(column=3, row=2)

btn_4 = Button(number_pad, text="4", command=btn_4_clicked)
btn_4.grid(column=1, row=1)

btn_5 = Button(number_pad, text="5", command=btn_5_clicked)
btn_5.grid(column=2, row=1)

btn_6 = Button(number_pad, text="6", command=btn_6_clicked)
btn_6.grid(column=3, row=1)

btn_7 = Button(number_pad, text="7", command=btn_7_clicked)
btn_7.grid(column=1, row=0)

btn_8 = Button(number_pad, text="8", command=btn_8_clicked)
btn_8.grid(column=2, row=0)

btn_9 = Button(number_pad, text="9", command=btn_9_clicked)
btn_9.grid(column=3, row=0)

btn_add = Button(number_pad, text="+", command=btn_add_clicked)
btn_add.grid(column=4, row=0)

btn_sub = Button(number_pad, text="-", command=btn_sub_clicked)
btn_sub.grid(column=4, row=1)

btn_mul = Button(number_pad, text="*", command=btn_mul_clicked)
btn_mul.grid(column=4, row=2)

btn_div = Button(number_pad, text="/", command=btn_div_clicked)
btn_div.grid(column=4, row=3)

btn_clear = Button(number_pad, text="C", command=btn_clear_clicked)
btn_clear.grid(column=2, row=3)

btn_calc = Button(number_pad, text="=", command=btn_calc_clicked)
btn_calc.grid(column=3, row=3)

window.mainloop()
