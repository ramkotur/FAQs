import unittest

from numpy import add


class test(unittest.TestCase):
    def testmultiple(self):
        self.assertEqual(add(2,3),5)

if __name__ == '__main__':
    unittest.main()