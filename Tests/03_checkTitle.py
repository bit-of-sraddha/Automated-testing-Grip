from selenium import webdriver
from selenium.webdriver.chrome.service import Service
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

# Check the page title
title = driver.title
if title == "The Sparks Foundation | Home":
    print("Page Title name is correct")
else:
    print("Wrong Title Name")

print("The test is completed")
driver.quit()
