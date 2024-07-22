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
driver.get("https://www.thesparksfoundationsingapore.org/about/executive-team/")

try:
    # Check if the first image exists and is visible
    elem1 = driver.find_element(By.XPATH, "/html/body/div[2]/div/div[1]/div/div[1]/a/img")
    if elem1.is_displayed():
        print("First Executive Team member image exists")
    else:
        print("First Executive Team member image is missing")

    # Check if the second image exists and is visible
    elem2 = driver.find_element(By.XPATH, "/html/body/div[2]/div/div[1]/div/div[3]/a/img")
    if elem2.is_displayed():
        print("Second Executive Team member image exists")
    else:
        print("Second Executive Team member image is missing")

except Exception as e:
    print("An error occurred while checking images:")
    print(f"Error: {e}")

# Clean up
time.sleep(2)
driver.quit()
print("The test is completed")
