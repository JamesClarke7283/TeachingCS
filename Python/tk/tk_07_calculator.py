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

result_lbl = Label(calc_frame, text="", width=35, borderwidth=5, background="white")
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


NUMBER_BTN_X = 40
NUMBER_BTN_Y = 20

number_buttons = [
 Button(number_pad, text=str(i), padx=NUMBER_BTN_X, pady=NUMBER_BTN_Y, command=lambda x=i: number_btn_clicked(str(x)))
 for i in range(10)
]

for i, button in enumerate(number_buttons[::-1]):
    button.grid(row=0 + (i // 3), column=(i % 3))

CALC_BTN_X = 39
CALC_BTN_Y = 20

btn_add = Button(number_pad, text="+", padx=CALC_BTN_X, pady=CALC_BTN_Y, command=lambda: op_btn_clicked(Operation.ADD))
btn_add.grid(column=3, row=0)

btn_sub = Button(number_pad, text="-", padx=CALC_BTN_X, pady=CALC_BTN_Y, command=lambda: op_btn_clicked(Operation.SUB))
btn_sub.grid(column=3, row=1)

btn_mul = Button(number_pad, text="×", padx=CALC_BTN_X, pady=CALC_BTN_Y, command=lambda: op_btn_clicked(Operation.MUL))
btn_mul.grid(column=3, row=2)

btn_div = Button(number_pad, text="÷", padx=CALC_BTN_X, pady=CALC_BTN_Y, command=lambda: op_btn_clicked(Operation.DIV))
btn_div.grid(column=3, row=3)

btn_clear = Button(number_pad, text="C", padx=CALC_BTN_X, pady=CALC_BTN_Y, command=btn_clear_clicked)
btn_clear.grid(column=1, row=3)

btn_calc = Button(number_pad, text="=", padx=CALC_BTN_X, pady=CALC_BTN_Y, command=btn_calc_clicked)
btn_calc.grid(column=2, row=3)

window.mainloop()
