import time

from selenium import webdriver
from selenium.webdriver.common.by import By

browser= webdriver.Chrome()
browser.get('https://practice.microdegree.work')
# browser.find_element(By.XPATH,'html/body/div/div/div/div/div/div/div/div/button').click()
# browser.find_element(By.XPATH,'//input').send_keys("rakesh")
# browser.find_element(By.XPATH,'//input').clear()
# browser.find_element(By.XPATH,'//input').send_keys("rakesh kothari")
# browser.find_element(By.XPATH,'//input[@id="idname"]').send_keys("rakesh")
browser.find_element(By.XPATH,'//*[@id="exampleInputName"]').send_keys("rakesh")





time.sleep(100)