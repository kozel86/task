import unittest
from airline import AirLine


class MyTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.my_number = AirLine('москва', '№47', '18:20', 'вторник')

    def test_single(self):
        self.assertIn('москва', self.my_number.dest())
        self.assertIn('№47', self.my_number.num())
        self.assertIn('18:20', self.my_number.time_f())
        self.assertIn('вторник', self.my_number.day())


if __name__ == '__main__':
    unittest.main()
