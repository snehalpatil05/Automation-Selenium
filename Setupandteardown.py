import unittest
from selenium import webdriver

class AmazonTesting(unittest.TestCase):

    @classmethod
    def setUp(cls):
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
    def tearDown(cls):
        print("This is Logout for Amazon")

if __name__=="__main__":
    unittest.main()