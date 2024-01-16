import time
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
import sys

class GoogleSearchEngine(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.browser = webdriver.Chrome()

    def setUp(self):
        self.browser.get('https://www.google.com/')
        self.browser.implicitly_wait(10)

    def tearDown(self):
        time.sleep(2)

    @classmethod
    def tearDownClass(cls):
        cls.browser.quit()

    def testcase1_searchPuneeth(self):
        self.browser.find_element(By.NAME, 'q').send_keys("Puneeth Rajkumar")
        self.browser.find_element(By.NAME, 'btnK').click()

    def testcase2_searchMicroDegree(self):
        self.browser.find_element(By.NAME, 'q').send_keys("Micro Degree Kannada")
        self.browser.find_element(By.NAME, 'btnK').click()

    def testcase3_searchPythonTutorial(self):
        self.browser.find_element(By.NAME, 'q').send_keys("python tutorial")
        self.browser.find_element(By.NAME, 'btnK').click()

    def testcase4_searchW3schools(self):
        self.browser.find_element(By.NAME, 'q').send_keys("w3schools")
        self.browser.find_element(By.NAME, 'btnK').click()

if __name__ == "__main__":
    # Specify the path for the reports folder
    report_folder = './Reports'

    # Run the test with the built-in HTML test runner
    loader = unittest.TestLoader()
    suite = loader.loadTestsFromTestCase(GoogleSearchEngine)

    runner = unittest.TextTestRunner(stream=sys.stdout)
    runner.run(suite)
