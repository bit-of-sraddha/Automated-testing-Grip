from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

print("Sample test case started")
chromedriver_path = "E:\selenium-webTesting-master\selenium-webTesting-master\selenium-webTesting-master\Browsers\chromedriver.exe"

service = Service(executable_path=chromedriver_path)

driver = webdriver.Chrome(service=service)
driver.maximize_window()

driver.get("https://www.google.com/")

search_box = driver.find_element(By.NAME, "q")
search_box.send_keys("sparks foundation")
time.sleep(3)

search_box.send_keys(Keys.ENTER)
time.sleep(3)

print("Sample test case successfully completed")

driver.quit()
