import unittest
from numpy import add

class TestAddFunction(unittest.TestCase):

    def test_add_positive_numbers(self):
        self.assertEqual(add(2, 3), 6)

    def test_add_negative_numbers(self):
        self.assertEqual(add(-1, -1), -2)

    def test_add_positive_and_negative_numbers(self):
        self.assertEqual(add(2, -3), -1)


if __name__ == '__main__':
    unittest.main()