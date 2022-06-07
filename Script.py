from selenium import webdriver
from selenium.webdriver.common.keys import Keys

import time

driver = webdriver.Chrome('Drivers/chromedriver')
driver.get("URL")
print(driver.title)
time.sleep(10)
search_bar = driver.find_element_by_name('text')
search_bar.clear()
search_bar.send_keys("Your Username")
search_bar.send_keys(Keys.RETURN)
time.sleep(5)
search_bar = driver.find_element_by_name('text')
search_bar.clear()
search_bar.send_keys("Your Username")
search_bar.send_keys(Keys.RETURN)
time.sleep(5)
search_bar = driver.find_element_by_name('password')
search_bar.clear()
search_bar.send_keys("Your Password")
search_bar.send_keys(Keys.RETURN)

driver.close()


