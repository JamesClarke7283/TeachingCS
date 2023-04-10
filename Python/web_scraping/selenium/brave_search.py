from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
import json


def search_brave(driver, search_query):

    driver.get('https://search.brave.com/')

    wait = WebDriverWait(driver, 10)
    wait.until(EC.presence_of_element_located((By.ID, 'searchbox')))

    # Find the search bar
    driver.find_element(By.ID, 'searchbox').send_keys(search_query)

    # Find the search button
    search_btn = driver.find_element(By.ID, 'submit-button')
    if search_btn:
        search_btn.click()
    else:
        print('Search button not found')

    # Wait for the results to load
    wait = WebDriverWait(driver, 10)
    wait.until(EC.presence_of_element_located((By.ID, 'results')))

    # Find the results
    results = driver.find_elements(By.CSS_SELECTOR, '.snippet.fdb')
    print(f'Found {len(results)} results')
    # Get the results data
    results_data = []
    for result in results:
        result_title = result.find_element(By.CLASS_NAME, 'snippet-title').text
        result_url = result.find_element(By.TAG_NAME, 'a').get_attribute('href')
        result_description = result.find_element(By.CLASS_NAME, 'snippet-description').text
        rd = {'title': result_title, 'url': result_url, 'description': result_description}
        results_data.append(rd)

    # Close the browser
    driver.quit()

    return results_data


def main():
    service = Service()

    # Initialize the WebDriver with the service object
    driver = webdriver.Chrome(service=service)
    
    search_query = 'Python'
    results = search_brave(search_query)
    print(json.dumps(results, indent=4))


if __name__ == '__main__':
    main()