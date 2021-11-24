import unittest
from sample.isPangram import *
from parameterized import parameterized, parameterized_class


class isPangramParameterizedPackage(unittest.TestCase):

    def setUp(self):
        self.tmp = isPangram()

    @parameterized.expand([
        ("abCdEfGhijKLmnOpqrsTUvWxyz", True),
        ("", False),
    ])
    def test_one_parameterized(self, word, expected):
        self.assertEqual(self.tmp.func(word), expected)


@parameterized_class(('word', 'expected'), [
        ("Two driven jocks help fax my big quiz.", True),
        (True, False),
        ("Jackdaws love my big sphinx of quartz.", True),
])
class FizzBuzzParameterizedPackage2(unittest.TestCase):
    def setUp(self):
        self.tmp = isPangram()

    def test_second_parameterized(self):
        self.assertEqual(self.tmp.func(self.word), self.expected)


if __name__ == '__main__':
    unittest.main()
