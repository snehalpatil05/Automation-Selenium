import unittest

class FirstTestCase(unittest.TestCase):
    def test_myfirsttestcase(self):
        print("This is my first testcase")

if __name__=="__main__":
    unittest.main()