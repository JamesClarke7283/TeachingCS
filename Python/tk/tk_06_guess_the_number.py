from tkinter import Tk, ttk
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

    def display_out(self, text, colour):
        self.number_lbl.configure(text=text, foreground=colour)

    def submited(self):
        usr_input = self.inp_txt.get()
        logging.info(f"Submitting Input: {usr_input}")
        if self.tries == 0:
            self.display_out("Ran out of attempts, game over!", "red")

        if usr_input.isnumeric():
            if int(usr_input) == self.answer:
                self.display_out("Correct!!", "green")
            else:
                filler = comp_incorrect(int(usr_input), self.answer)
                self.display_out(f"Incorrect,{filler}, Try again ({self.tries} lives left)", "yellow")
                self.tries -= 1

            logging.info("Number is Numeric, submit answer")
        else:
            self.display_out("ERROR: text must be a number", "red")


    def __init__(self):
        self.answer = random.randint(1, 20)
        self.tries = 6
        self.window = Tk()
        self.window.title("Guess the number (Guess Between 1-20)")
        self.window.geometry('450x200')

        # Top
        self.number_lbl = ttk.Label(self.window, text="0", font="24px")
        self.number_lbl.pack(side="top", expand=1)

        # Input

        self.input_frm = ttk.Frame(self.window)
        self.input_frm.pack(side="bottom", expand=1)

        self.inp_txt = ttk.Entry(self.input_frm)
        self.inp_txt.pack(side="top")

        self.submit_btn = ttk.Button(self.input_frm, text="Submit", command=self.submited)
        self.submit_btn.pack(side="bottom")

        self.window.mainloop()

if __name__ == "__main__":
    gtn = GTN_UI()
