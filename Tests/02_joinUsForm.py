from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
import time

# User data
fullname = "Sushree Sangita Das"
email = "sraddha1736@gmail.com"

# Path to your ChromeDriver
PATH = "E:\selenium-webTesting-master\selenium-webTesting-master\selenium-webTesting-master\Browsers\chromedriver.exe"

# Create a Service object
service = Service(executable_path=PATH)

# Initialize the Chrome driver with the Service object
driver = webdriver.Chrome(service=service)
driver.maximize_window()
driver.get("https://www.thesparksfoundationsingapore.org/join-us/why-join-us/#")

try:
    # Fill out the form
    driver.find_element(By.XPATH, "/html/body/div[2]/div/div[2]/div[2]/div/form/input[1]").send_keys(fullname)
    time.sleep(3)

    driver.find_element(By.XPATH, "/html/body/div[2]/div/div[2]/div[2]/div/form/input[2]").send_keys(email)
    time.sleep(3)

    # Select an option from the dropdown
    dropdown = Select(driver.find_element(By.XPATH, "/html/body/div[2]/div/div[2]/div[2]/div/form/select"))
    dropdown.select_by_index(1)  # Select the second option (index starts at 0)
    time.sleep(3)

    # Submit the form
    driver.find_element(By.XPATH, "/html/body/div[2]/div/div[2]/div[2]/div/form/input[@type='submit']").send_keys(Keys.RETURN)
    time.sleep(3)

    print("The test is completed successfully by submitting form data")

finally:
    # Clean up
    driver.quit()
