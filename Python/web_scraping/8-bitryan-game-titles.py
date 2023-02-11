# 8-bitryan game titles
from bs4 import BeautifulSoup
import requests

# Author: Anon <anonymouse@james-clarke.ynh.fr>>

# Set the URL you want to webscrape from
url = "https://yewtu.be/channel/UCx8vbgWs666cAS7wsKos5sA"

# Get the HTML from the URL
r = requests.get(url)

# Parse the HTML
soup = BeautifulSoup(r.text, "html.parser")

# Get the titles of the videos
title_selector = "div.pure-u-md-1-4 > div > a > p:nth-of-type(1)"
unfiltered_titles = soup.select(title_selector)

# Initialize empty lists
video_titles = []
game_titles = []

# Loop through the titles and add them to the list
for i in unfiltered_titles:
    video_titles.append(i.text)

# Loop through the video titles and get the game titles
for i in video_titles:
    # Removes the brackets and everything inside them
    video_title = i.split('(')[0].strip()
    # Splits the string by the pipe character to get the game title
    video_title = video_title.split('|')
    if len(video_title) >= 2:
        game_titles.append(video_title[1])
print(game_titles)
