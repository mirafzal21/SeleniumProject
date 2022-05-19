from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()

driver.get("http://automationpractice.com")
time.sleep(5)

search_box = driver.find_element(By.NAME, 'search_query')
search_box.send_keys("dress")
time.sleep(5)

# clicking the search button, finding by XPATH
# driver.find_element(By.XPATH, "//button[@name='submit_search']").click()
# "//tag[@attribute='value of attribute' and @attribute2='value2']

search_box = driver.find_element(By.CSS_SELECTOR, 'button.button-search').click()

time.sleep(5)
# click the Signin button
driver.find_element(By.PARTIAL_LINK_TEXT, 'Sign in').click()
