import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
browser=webdriver.Chrome()
browser.get('https://www.marutisuzuki.com/dealer-showrooms')
ShowroomDropdown=Select(browser.find_element(By.ID, 'select-dealer-locator'))
# ShowroomDropdown.select_by_visible_text('Service Workshop')
# ShowroomDropdown.select_by_value('TVS')
# print(len(ShowroomDropdown.options))
for eachShowroom in ShowroomDropdown.options:
    print(eachShowroom.text)

time.sleep(100)
browser.quit()