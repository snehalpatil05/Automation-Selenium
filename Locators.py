import time
from selenium import webdriver
from selenium.webdriver.common.by import By

browser=webdriver.Chrome()
browser.get('https://courses.microdegree.work/')
# browser.find_element(By.CLASS_NAME,"header__nav-sign-in").click()


#id
# browser.find_element(By.ID,"ap_email").send_keys('email@gmail.com')
#
#name
browser.find_element(By.NAME,"email").send_keys('snehal@gmail.com')
#
#class
# browser.find_element(By.CLASS_NAME,"form__control input--error").send_keys('snehal@gmail.com')

#tag
browser.find_element(By.TAG_NAME,'a').click()
time.sleep(10)
browser.quit()