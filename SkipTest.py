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
    def setUp(cls):
        print("This is Amazon Login")

    @unittest.SkipTest
    def test1_account(self):
        print("this is Account flow test")

    @unittest.skip("Skipping this Test case because the functionality is not yet ready")
    def test2_orders(self):
        print("This is search test2")

    @unittest.skipIf("link"=="link", "Link Avaialble")
    def test3_wishlist(self):
        print("This is search test3")

    def test4_recommendations(self):
        print("This is search test4")

    def test5_primemembership(self):
        print("This is search test5")

    @classmethod
    def tearDown(cls):
        print("This is Logout for Amazon")

    @classmethod
    def tearDownClass(cls):
        print("Close the Application - Closing browser using webdriver")

if __name__=="__main__":
    unittest.main()