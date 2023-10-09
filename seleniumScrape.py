from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import time;
path = '/Users/sunny/Desktop/chromedriver-mac-arm64/chromedriver'
#Create service object
s = Service(path)

driver = webdriver.Chrome(service=s)

#Navigate to page and let it load
driver.get("https://catalog.mtroyal.ca/content.php?catoid=31&navoid=2496")
time.sleep(1)

for page_number in range(2,19):
    course_Previews = driver.find_elements(By.XPATH, "//a[contains(@onclick, 'showCourse') or contains(@onclick, 'showCatalogData')]")
    
    # Click on each course preview to load the description
    for preview in course_Previews:
        preview.click()
        time.sleep(0.3)

    # Wait for all descriptions to load
    time.sleep(2)

    #Easiest way to find all <div> elements that contain course descriptions is to find all <div> elements that contain <h3> elements that are not in the footer
    course_divs = driver.find_elements(By.XPATH,'//div[h3[not(ancestor::footer)]]')
    
    # Write each course description to file. Opens in append mode because we are scraping multiple pages.
    with open('courseDescriptions.txt', 'a', encoding='utf-8') as f:
        for course_div in course_divs:
            try:
                description = course_div.text.strip()
            except Exception:
                description = 'Not available'
            f.write(f'Description: {description}\n')
            f.write('---\n')

    # Go to next page
    try:
        xpath = f'//a[@aria-label="Page {page_number}"]'
        element = driver.find_element(By.XPATH, xpath)
        # Do something with the element, like clicking it to go to the next page
        element.click()
        time.sleep(1)
    except NoSuchElementException:
        print(f'Element with page number {page_number} not found.')
        break  # or continue, depending on your needs

driver.quit()

