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


def number_btn_clicked(number: str):
    current_text = result_lbl['text']
    result_lbl.config(text=current_text+number)


def op_btn_clicked(operation: Operation):
    global accumulator
    global op
    accumulator = int(result_lbl['text'])
    result_lbl.config(text="")
    op = operation


def btn_clear_clicked():
    result_lbl.config(text="")


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


btn_0 = Button(number_pad, text="0", command=lambda: number_btn_clicked("0"))
btn_0.grid(column=1, row=3)

btn_1 = Button(number_pad, text="1", command=lambda: number_btn_clicked("1"))
btn_1.grid(column=1, row=2)

btn_2 = Button(number_pad, text="2", command=lambda: number_btn_clicked("2"))
btn_2.grid(column=2, row=2)

btn_3 = Button(number_pad, text="3", command=lambda: number_btn_clicked("3"))
btn_3.grid(column=3, row=2)

btn_4 = Button(number_pad, text="4", command=lambda: number_btn_clicked("4"))
btn_4.grid(column=1, row=1)

btn_5 = Button(number_pad, text="5", command=lambda: number_btn_clicked("5"))
btn_5.grid(column=2, row=1)

btn_6 = Button(number_pad, text="6", command=lambda: number_btn_clicked("6"))
btn_6.grid(column=3, row=1)

btn_7 = Button(number_pad, text="7", command=lambda: number_btn_clicked("7"))
btn_7.grid(column=1, row=0)

btn_8 = Button(number_pad, text="8", command=lambda: number_btn_clicked("8"))
btn_8.grid(column=2, row=0)

btn_9 = Button(number_pad, text="9", command=lambda: number_btn_clicked("9"))
btn_9.grid(column=3, row=0)

btn_add = Button(number_pad, text="+", command=lambda: op_btn_clicked(Operation.ADD))
btn_add.grid(column=4, row=0)

btn_sub = Button(number_pad, text="-", command=lambda: op_btn_clicked(Operation.SUB))
btn_sub.grid(column=4, row=1)

btn_mul = Button(number_pad, text="×", command=lambda: op_btn_clicked(Operation.MUL))
btn_mul.grid(column=4, row=2)

btn_div = Button(number_pad, text="÷", command=lambda: op_btn_clicked(Operation.DIV))
btn_div.grid(column=4, row=3)

btn_clear = Button(number_pad, text="C", command=btn_clear_clicked)
btn_clear.grid(column=2, row=3)

btn_calc = Button(number_pad, text="=", command=btn_calc_clicked)
btn_calc.grid(column=3, row=3)


window.mainloop()
