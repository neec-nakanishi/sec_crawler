from selenium import webdriver
import time
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get('https://search.yahoo.co.jp/search')
time.sleep(3)

element = driver.find_element(By.NAME, "p")
element.send_keys("python")
element.submit()
time.sleep(100)
driver.quit()