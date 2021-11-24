from sample.isPangram import *
import unittest

class isPangramTest(unittest.TestCase):
    def setUp(self):
        self.temp = isPangram()

    def test_isPangram_correct(self):
        self.assertEqual(self.temp.func('abcdefghijklmnopqrstuvwxyz'), True)

    def test_isPangram_correct_sentence(self):
        self.assertEqual(self.temp.func('The quick brown fox jumps over a lazy dog.'), True)

    def test_isPangram_incorrect(self):
        self.assertEqual(self.temp.func('abcdefghtuvwxyz'), False)

    def test_isPangram_empty_string(self):
        self.assertEqual(self.temp.func(''), False)

    def test_isPangram_empty_array(self):
        self.assertEqual(self.temp.func([]), False)

    def test_isPangram_integer(self):
        self.assertEqual(self.temp.func(45), False)

    def test_isPangram_float(self):
        self.assertEqual(self.temp.func(123.45321), False)

    def test_isPangram_None(self):
        self.assertEqual(self.temp.func(None), False)

if __name__ == '__main__':
    unittest.main()
