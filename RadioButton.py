import time
from selenium import webdriver
from selenium.webdriver.common.by import By
browser=webdriver.Chrome()
# browser.get('https://www.nexaexperience.com/e-booking?login=0&_gl=1*1mg460y*_ga*NTgyNDU4MzUxLjE3MDQ4NzY4NjI.*_ga_RM5D6V43B5*MTcwNDk1MDEwNC4yLjEuMTcwNDk1MDEzOC4yNi4wLjA.&_ga=2.204766608.1216555568.1704876862-582458351.1704876862&_gac=1.187875802.1704876894.CjwKCAiA-vOsBhAAEiwAIWR0TYKbx0CmpDqxUuwf88X6ti7gWny9dJp6bb3mBwsRDrwXrHXoYmjtsBoCaNIQAvD_BwE')
# #checkbox
# status=browser.find_element(By.ID, 'ebboking-disclaimer-step1').is_selected()
# print(status)
# browser.find_element(By.ID, 'ebboking-disclaimer-step1').click()
# print(browser.find_element(By.ID, 'ebboking-disclaimer-step1').is_selected())

#radioButton
browser.get('https://ebiz.licindia.in/D2CPM/#Login')
# status=browser.find_element(By.ID, 'radio-1504-inputEl').is_selected()
# print(status)
browser.find_element(By.ID, 'radio-1504-boxLabelEl').click()
# print(browser.find_element(By.ID, 'radio-1504-inputEl').is_selected())
# browser.find_element(By.XPATH, '//*[@id="radio-1504-inputEl"]').click()

time.sleep(100)
browser.quit()