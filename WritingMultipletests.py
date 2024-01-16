import unittest
from selenium import webdriver

class PageTitleTest(unittest.TestCase):
    def test1_googlePageTitle(self):
        self.browser = webdriver.Chrome()
        self.browser.get('https://www.google.com/')
        print("Title of Google is "+ self.browser.title)
        self.browser.close()

    def test2_yahooPageTitke(self):
        self.browser = webdriver.Chrome()
        self.browser.get('https://www.yahoo.com/')
        print("Title of Yahoo is "+ self.browser.title)
        self.browser.close()


if __name__ == "__main__":
    unittest.main()