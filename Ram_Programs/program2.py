from unittest import TestCase
from numpy import divide

class TestFunctions(TestCase):
    def test_devide_result(self):
        dividend=15
        divisor=3
        expected_result=5.0
        self.assertAlmostEqual(divide(dividend,divisor),expected_result,delta=0.0001)

