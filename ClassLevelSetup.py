import unittest
from selenium import webdriver

def setUpModule():
    print("In Setup module - import details - data")

def tearDownModule():
    print("In Tear down module - closes the data file")

class AmazonTesting(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print("Open Application - Open Chrom Browser using driver")

    @classmethod
    def setUp(self):
        print("This is Amazon Login")

    def test1_account(self):
        print("this is Account flow test")

    def test2_orders(self):
        print("This is search test2")

    def test3_wishlist(self):
        print("This is search test3")

    def test4_recommendations(self):
        print("This is search test4")

    def test5_primemembership(self):
        print("This is search test5")

    @classmethod
    def tearDown(self):
        print("This is Logout for Amazon")

    @classmethod
    def tearDownClass(cls):
        print("Close the Application - Closing browser using webdriver")

if __name__=="__main__":
    unittest.main()