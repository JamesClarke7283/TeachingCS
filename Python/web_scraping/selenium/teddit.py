from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.firefox.service import Service
import json

def get_links(driver):
    # Select elements on the page
    sublinks_element = driver.find_element(By.CLASS_NAME, "sublinks")

    # Get the links from the sublinks element
    links_elements = sublinks_element.find_elements(By.TAG_NAME, "a")

    # Create a list of links
    links = {}
    for link_element in links_elements:
        links[link_element.text] = link_element.get_attribute("href")

    return links


def query(driver):
    # Search the page
    query = "python"
    driver.get(f"https://tedd.it/r/all/search?q={query}&restrict_sr=on&nsfw=on&sort=relevance&t=all&after=")

    # Wait for the page to load
    cards_element = driver.find_element(By.ID, "links")

    # Get cards from the cards element
    card_elements = cards_element.find_elements(By.CLASS_NAME, "link")

    # Create a list of cards
    cards = []
    for card_element in card_elements:
        # Get the card data

        wait = WebDriverWait(card_element, 10)
        wait.until(EC.visibility_of_element_located((By.XPATH, ".//div[contains(@class, 'image')]")))

        # Get the upvotes
        upvotes = card_element.find_element(By.XPATH, "./div[contains(@class, 'upvotes')]/span").text

        # Get the image url
        # image = card_element.find_element(By.XPATH, ".//div[contains(@class, 'image')]/a/img").get_attribute("src")

        # Get the entry element
        entry_element = card_element.find_element(By.XPATH, "./div[contains(@class,'entry')]")

        # Get the title and link
        title = entry_element.find_element(By.XPATH, "./div[contains(@class,'title')]/a/h2").text
        link = entry_element.find_element(By.XPATH, "./div[contains(@class,'title')]/a").get_attribute("href")

        # Get the meta element
        meta_element = entry_element.find_element(By.XPATH, "./div[contains(@class,'meta')]")

        submitted_element = meta_element.find_element(By.XPATH, "./p[contains(@class,'submitted')]")

        # Get the date submitted
        date_submitted = submitted_element.find_element(By.XPATH, "./span").get_attribute("title")

        # Get the author
        author_link = submitted_element.find_element(By.XPATH, "./a").get_attribute("href")
        author_name = submitted_element.find_element(By.XPATH, "./a").text

        # Get the subreddit
        subreddit_link = meta_element.find_element(By.XPATH, "./p[contains(@class,'to')]/a").get_attribute("href")
        subreddit_name = meta_element.find_element(By.XPATH, "./p[contains(@class,'to')]/a").text

        # Get the comments
        comments_element = meta_element.find_element(By.XPATH, "./div[contains(@class,'links')]")

        # Get the number of comments
        n_comments = int(comments_element.find_element(By.XPATH, "./a[contains(@class,'comments')]").text.replace(" comments", ""))
        comments_link = comments_element.find_element(By.XPATH, "./a[contains(@class,'comments')]").get_attribute("href")

        # Put the properties in a dictionary
        card = {"title": title, "link": link, "upvotes": upvotes, "date_submitted": date_submitted, "author": {"name": author_name, "link": author_link}, "subreddit": {"name": subreddit_name, "link": subreddit_link}, "comments": {"n_comments": n_comments, "link": comments_link}}
        cards.append(card)
    return cards


def main():
    service = Service()

    # Initialize the WebDriver with the service object
    driver = webdriver.Firefox(service=service)

    # Get the driver to navigate to a page
    driver.get("https://tedd.it/")

    links = get_links(driver)
    print(json.dumps(links, indent=4))

    cards = query(driver)
    print(json.dumps(cards, indent=4))
    # Quits the driver and closes every associated window
    driver.quit()




if __name__ == '__main__':
    main()