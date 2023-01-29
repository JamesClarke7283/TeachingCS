import tkinter as tk
import random

root = tk.Tk()
root.title("Roll the Dice")


def roll_dice():
    number = random.randint(1, 6)
    result_label.config(text=f"You rolled a {number}")
    result_image.config(file=f"images/die_{number}.png")


result_label = tk.Label(root, text="Roll the dice to see the result.")
result_label.pack()

result_image = tk.PhotoImage(file="images/die_1.png")
image_label = tk.Label(root, image=result_image)
image_label.pack()

roll_button = tk.Button(root, text="Roll", command=roll_dice)
roll_button.pack()

root.mainloop()
