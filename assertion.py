import unittest
from selenium import webdriver

class TitleTesting(unittest.TestCase):

    # def test1_googlePageTitle(self):
    #     browser = webdriver.Chrome()
        # browser.get('https://www.google.com/')
        # pageTitle = browser.title
        # self.assertEquals('Google', pageTitle, 'Page title is not as expected')
        # self.assertNotEqual('Google12', pageTitle, 'Page title is as expected')
        # self.assertTrue('Google'==pageTitle,'Page title is wrong')
        # self.assertFalse('Google3' == pageTitle, 'Page title is Same')

        #NoneChecking->
    # def test2_assertNoneCheck(self):
        # browser=None
        # self.assertIsNone(browser)

        # NotNone->
    # def test3_assertNotNoneCheck(self):
        # self.assertIsNotNone(browser)

        #AssertIn
     # def test4_assertInCheck(self):
        # list = ("Bengaluru", "Mangaluru","Shivmoga", "Hubli")
        # self.assertIn("Hubli", list)
    # def test5_assertInCheck(self):
        # list = ("Bengaluru", "Mangaluru","Shivmoga", "Hubli")
        # self.assertIn("Hubbli", list)

        #ASSERTNOTIN
    # def test6_assertNotInCheck(self):
        # self.assertNotIn("Hubbli", list)

    def test7_assertGreaterCheck(self):
        # self.assertGreater(500,1000, "test failed")
        # self.assertGreaterEqual(1500,1500, "test failed")

        # self.assertLess(500,1000, "test failed")
        self.assertLessEqual(1000,1000, "test failed")






if __name__=="__main__":
    unittest.main()