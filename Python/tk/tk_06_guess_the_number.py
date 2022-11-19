from tkinter import Tk, ttk, HORIZONTAL
import logging
from os import environ as os_environ
import random

LOGLEVEL = os_environ.get('LOGLEVEL', 'INFO').upper()
logging.basicConfig(level=LOGLEVEL)

""" Does comparison of answer and guess,
    when the value is incorrect and returns
    a description in plain text """


def comp_incorrect(guess, answer):
    if guess > answer:
        return "too high"
    elif guess < answer:
        return "too low"


class GTN_UI:
    RANGE_START = 1
    RANGE_END = 20
    LIVES = 6

    def scale_moved(self, scale_inp):
        """Triggers when the scale bar is moved, changes the label to value selected"""
        self.scale_value = round(float(scale_inp))
        logging.debug(f"Value of scale is {self.scale_value}")
        self.scale_lbl.configure(text=str(self.scale_value))

    def display_out(self, text, colour):
        """Displays text out on the screen"""
        self.number_lbl.configure(text=text, foreground=colour)

    def submitted(self):
        """Triggers when user presses submit button"""
        usr_input = self.scale_value
        logging.info(f"Submitting Input: {usr_input}")
        if self.tries <= 0:
            self.display_out("Ran out of attempts, game over!", "red")
        elif int(usr_input) == self.answer:
            self.display_out("Correct!!", "green")
        else:
            filler = comp_incorrect(int(usr_input), self.answer)
            self.display_out(f"Incorrect, {filler}, Try again ({self.tries} lives left)", "yellow")
            self.tries -= 1

    def __init__(self):
        self.scale_value = 0
        self.answer = random.randint(self.RANGE_START, self.RANGE_END)
        self.tries = self.LIVES
        self.window = Tk()
        self.window.title(f"Guess the number (Guess Between {self.RANGE_START}-{self.RANGE_END})")
        self.window.geometry('450x200')

        # Top
        self.number_lbl = ttk.Label(self.window, text="0", font="24px")
        self.number_lbl.pack(side="top", expand=1)

        # Input

        self.input_frm = ttk.Frame(self.window)
        self.input_frm.pack(side="bottom", expand=1)

        self.submit_btn = ttk.Button(self.input_frm, text="Submit", command=self.submitted)
        self.submit_btn.pack(side="bottom")

        # Scale Frame

        self.scale_frm = ttk.Frame(self.input_frm)
        self.scale_frm.pack(side="bottom")

        self.scale_lbl = ttk.Label(self.scale_frm, text="0")
        self.scale_lbl.pack(side="top")

        self.inp_scl = ttk.Scale(self.scale_frm, orient=HORIZONTAL, length=200,
                                 from_=self.RANGE_START, to=self.RANGE_END,
                                 command=self.scale_moved)

        self.inp_scl.pack(side="bottom")

        self.window.mainloop()


if __name__ == "__main__":
    gtn = GTN_UI()
