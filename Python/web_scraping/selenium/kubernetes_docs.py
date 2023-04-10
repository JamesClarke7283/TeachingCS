from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
import json


def get_cards(driver, kubernetes_docs_url):
    driver.get(kubernetes_docs_url)

    wait = WebDriverWait(driver, 10)
    wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'launch-cards')))

    # Find the cards
    cards = driver.find_elements(By.CLASS_NAME, 'launch-card')

    # Iterate through cards and get
    launchcards_data = []
    for card in cards:
        card_title = card.find_element(By.TAG_NAME, "h2").text
        card_description = card.find_element(By.TAG_NAME, "p").text
        card_urls_list_element = card.find_element(By.TAG_NAME, "ul")
        card_url_elements = card_urls_list_element.find_elements(By.TAG_NAME, "li")
        # Iterate through the urls and get the url and title and set the url element to a dict
        for index, url_element in enumerate(card_url_elements):
            url_element = url_element.find_element(By.TAG_NAME, "a")
            url = url_element.get_attribute("href")
            title = url_element.text
            card_url_elements[index] = {"url": url, "title": title}
        # Create the card data dict
        item_data = {"title": card_title, "description": card_description, "urls": card_url_elements}

        # Append the card data to the launchcards_data list
        launchcards_data.append(item_data)

    return launchcards_data


def main():
    service = Service()

    # Initialize the WebDriver with the service object
    driver = webdriver.Chrome(service=service)

    kubernetes_docs_url = 'https://kubernetes.io/docs/home/'
    cards = get_cards(driver, kubernetes_docs_url)
    print(json.dumps(cards, indent=4))


if __name__ == '__main__':
    main()