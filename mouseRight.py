import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains

browser=webdriver.Chrome()
browser.get('https://www.selenium.dev/')
myActions = ActionChains(browser)
# myActions.context_click().perform()
myButton = browser.find_element(By.CLASS_NAME,'selenium-button selenium-webdriver text-uppercase fw-bold')
myActions.context_click(myButton).perform()
time.sleep(10)
browser.quit()