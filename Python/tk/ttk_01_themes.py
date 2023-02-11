import tkinter as tk
from tkinter import ttk
window = tk.Tk()

window.title("Welcome to My app")

style = ttk.Style()
s = style.theme_use("alt")

window.configure(style=s)



window.mainloop()