from bs4 import BeautifulSoup
import requests

url = "https://yewtu.be/channel/UCIe2pR6PE0dae9BunJ38F7w"

# Get the HTML from the URL
r = requests.get(url)

# Parse the HTML
soup = BeautifulSoup(r.text, "html.parser")

# Get the titles of the videos
title_selector = "div.pure-u-md-1-4 > div > a > p:nth-of-type(1)"
unfiltered_titles = soup.select(title_selector)

video_titles = []

# Loop through the titles and add them to the list
for i in unfiltered_titles:
    video_titles.append(i.text)

group = ["weight", "health", "diet", "exercise", "fitness", "nutrition"]
exclude_group = ["?", "review", "reviewing", "reviewed"]

filtered_titles = []
for title in video_titles:
    for keyword in group:
        if keyword.lower() in title.lower():
            count_matches = 0
            for exclude_keyword in exclude_group:
                    if exclude_keyword.lower() not in title.lower():
                        count_matches += 1
                    if count_matches == len(exclude_group):
                        filtered_titles.append(title)
                
print(filtered_titles)