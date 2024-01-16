import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains

browser=webdriver.Chrome()
browser.get('https://www.selenium.dev/')
target = browser.find_element()
action = ActionChains(browser)
action.double_click(target).perform()

time.sleep()
browser.quit()