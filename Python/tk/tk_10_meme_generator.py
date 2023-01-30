import tkinter as tk
import requests
from io import BytesIO
from PIL import Image, ImageTk
import json
from random import Random

# Create the GUI window
root = tk.Tk()
root.title("Meme Generator")

# Function to handle the button click


def create_meme():
    # API endpoint and parameters
    url = "https://api.imgflip.com/get_memes"
    response = requests.get(url)

    # Get the first meme from the API response
    memes = json.loads(response.text)["data"]["memes"]
    r = Random()
    meme_selection = r.randint(0, len(memes)-1)
    meme_url = memes[meme_selection]["url"]

    # Load the meme image
    response = requests.get(meme_url)
    image = Image.open(BytesIO(response.content))
    image = ImageTk.PhotoImage(image)

    # Display the meme in the label widget
    label.config(image=image)
    label.image = image


# Create the button and label widgets
button = tk.Button(root, text="Create Meme", command=create_meme)
label = tk.Label(root)

# Pack the widgets into the window
button.pack()
label.pack()

# Start the GUI event loop
root.mainloop()
