import time

from selenium import webdriver
from selenium.webdriver.common.by import By
browser=webdriver.Chrome()
browser.get('https://www.marutisuzuki.com/')
# print(browser.find_element(By.ID,"BaSV-Home-red").text)
browser.find_element(By.ID,"BaSV-Home-red").click()
browser.find_element(By.ID,'lad-footer').click()
time.sleep(100)
browser.quit()
