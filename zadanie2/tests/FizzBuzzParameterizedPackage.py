import unittest
from zadanie2.src.FizzBuzz import *
from parameterized import parameterized, parameterized_class
import math

class FizzBuzzParameterizedPackage(unittest.TestCase):

    def setUp(self):
        self.tmp = FizzBuzz()

    @parameterized.expand([
        ('a', Exception),
        ([], Exception),
        (12.34, Exception),
    ])
    def test_one_parameterized(self,argument, expected):
        self.assertRaises(expected, self.tmp.func, argument)


@parameterized_class(('number', 'expected'), [
        (1341, "Fizz"),
        (345, "FizzBuzz"),
        (11, "\"11\""),
])
class FizzBuzzParameterizedPackage2(unittest.TestCase):
    def setUp(self):
        self.tmp = FizzBuzz()

    def test_second_parameterized(self):
        self.assertEqual(self.tmp.func(self.number), self.expected)


if __name__ == '__main__':
    unittest.main()
