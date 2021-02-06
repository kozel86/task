import unittest
from zadanie1_funkcii import squares

class MyTest(unittest.TestCase):
    def test_1(self):
        self.assertEqual(squares(3,2),1,3)
    def test_2(self):
        self.assertEqual(squares(2,5),4,1)


if __name__ == '__main__':
    unittest.main()
