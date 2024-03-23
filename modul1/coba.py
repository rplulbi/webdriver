import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Edge()
driver.get('https://google.com')
time.sleep(2)
driver.quit()