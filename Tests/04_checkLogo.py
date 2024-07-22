from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

# Path to your ChromeDriver
PATH = "E:\selenium-webTesting-master\selenium-webTesting-master\selenium-webTesting-master\Browsers\chromedriver.exe"

# Create a Service object
service = Service(executable_path=PATH)

# Initialize the Chrome driver with the Service object
driver = webdriver.Chrome(service=service)
driver.maximize_window()

# Open the webpage
driver.get("https://www.thesparksfoundationsingapore.org/")

try:
    # Check if the logo exists
    elem = driver.find_element(By.XPATH, "/html/body/div[1]/div/div[1]/h1/a/img")
    if elem.is_displayed():
        print("Logo exists on the homepage")
    else:
        print("Logo is not visible on the homepage")
except Exception as e:
    print("Logo missing from homepage")
    print(f"Error: {e}")

# Clean up
time.sleep(2)
driver.quit()
print("The test is completed")
