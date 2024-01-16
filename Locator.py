import time

from selenium import webdriver
from selenium.webdriver.common.by import By

browser = webdriver.Chrome()
browser.get('https://practice.microdegree.work')
# browser.find_element(By.LINK_TEXT,'All Courses').click()
# browser.find_element(By.PARTIAL_LINK_TEXT,'All C').click()
# browser.find_element(By.CSS_SELECTOR, 'input#exampleInputName').send_keys("Rakesh")

# browser.find_element(By.CSS_SELECTOR, 'div button').click()
time.sleep(100)
