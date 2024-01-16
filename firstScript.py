import time
from selenium import webdriver

driver = webdriver.Chrome()
driver.get('https://practice.microdegree.work/')
# driver.find_element_by_id('root').click()
print(driver.current_url)

#TestCases:
actual_url=driver.current_url
expected_url='https://practice.microdegree.work/'

if actual_url==expected_url:
    print('Test Succesful')
else:
    print('failed')


input("Press Enter to close the browser...")
driver.quit()
