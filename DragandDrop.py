import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains

browser=webdriver.Chrome()
browser.get('https://www.selenium.dev/')
sourceElement = browser.find_element(By.ID,'') #Source Element
targetElement = browser.find_element(By.ID,'') #Target Element
action = ActionChains(browser)
action.drag_and_drop(sourceElement, targetElement).perform()

time.sleep()
browser.quit()