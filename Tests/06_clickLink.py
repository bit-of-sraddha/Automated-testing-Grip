from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

# Path to your ChromeDriver
PATH = "E:\selenium-webTesting-master\selenium-webTesting-master\selenium-webTesting-master\Browsers\chromedriver.exee"

# Create a Service object
service = Service(executable_path=PATH)

# Initialize the Chrome driver with the Service object
driver = webdriver.Chrome(service=service)
driver.maximize_window()

# Open the webpage
driver.get("https://www.thesparksfoundationsingapore.org/")
time.sleep(5)

# Click on "KNOW MORE" link
driver.find_element(By.LINK_TEXT, "KNOW MORE").click()
time.sleep(5)

# Click on "Executive Team" link
driver.find_element(By.LINK_TEXT, "Executive Team").click()

print("The test is completed")
driver.quit()
