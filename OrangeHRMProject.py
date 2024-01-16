import time
from selenium import webdriver
from selenium.webdriver.common.by import By
import unittest
import HtmlTestRunner

class TestOrangeHRMHomePage(unittest.TestCase):



    def testcase1_checkTitle(self):
        browser = webdriver.Chrome()
        browser.get('https://opensource-demo.orangehrmlive.com/web/index.php/auth/login')
        print(browser.title)
        time.sleep(5)
        browser.quit()

    def testcase2_checkLogin(self):
        browser = webdriver.Chrome()
        browser.get('https://opensource-demo.orangehrmlive.com/web/index.php/auth/login')
        time.sleep(2)
        browser.find_element(By.XPATH,'//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[1]/div/div[2]/input').send_keys('Admin')
        time.sleep(2)
        browser.find_element(By.XPATH,'//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[2]/div/div[2]/input').send_keys('admin123')
        time.sleep(2)
        browser.find_element(By.XPATH, '//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button').click()
        time.sleep(2)
        browser.quit()

    def testcase3_checkForgotPwdLink(self):
        browser = webdriver.Chrome()
        browser.get('https://opensource-demo.orangehrmlive.com/web/index.php/auth/login')
        time.sleep(2)
        browser.find_element(By.XPATH,'//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[4]/p').click()
        time.sleep(2)
        print(browser.current_url)
        browser.quit()


if __name__ == "__main__":
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='./reportOrangeHRM/'))
