from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import requests
import time

PATH = "E:\selenium-webTesting-master\selenium-webTesting-master\selenium-webTesting-master\Browsers\chromedriver.exe"

service = Service(executable_path=PATH)

chrome_options = Options()

driver = webdriver.Chrome(service=service, options=chrome_options)
driver.maximize_window()
driver.get('https://www.thesparksfoundationsingapore.org/programs/student-scholarship-program/')

links = driver.find_elements(By.CSS_SELECTOR, "a")
print("Total number of links --", len(links))

for link in links:
    href = link.get_attribute('href')
    if href:
        try:
            req = requests.head(href, allow_redirects=True)
            if req.status_code >= 400: 
                print(href, req.status_code)
            else:
                print(href + " -- OK")
        except requests.RequestException as e:
            print(f"Error checking {href}: {e}")
    else:
        print("No href attribute found for link")


time.sleep(2)
driver.quit()
print("The test is completed")
