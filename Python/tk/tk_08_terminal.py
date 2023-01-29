import tkinter as tk
from tkinter import Entry
import subprocess


def run_command():
    command = input_field.get()
    result = subprocess.run(command, shell=True, stdout=subprocess.PIPE)
    output_field.insert("end", result.stdout.decode())


root = tk.Tk()
root.title("Terminal App")

input_field = Entry(root)
input_field.pack()

run_button = tk.Button(root, text="Run Command", command=run_command)
run_button.pack()

output_field = tk.Text(root)
output_field.pack()

root.mainloop()
