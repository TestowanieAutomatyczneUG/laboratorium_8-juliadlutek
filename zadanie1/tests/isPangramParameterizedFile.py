import unittest
from sample.isPangram import *

class isPangramParameterizedFile(unittest.TestCase):

    def test_from_file(self):
      fileTest = open("data/is_pangram_data_test")
      tmpIsPangram = isPangram()
      for line in fileTest:
        if line.startswith("#") or line.startswith(" ") or line.startswith("\n"):
            continue
        else:
            data = line.split(" ")
            inp, result = data[0], bool(data[1].strip("\n"))
            self.assertEqual(tmpIsPangram.func(inp), result)
      fileTest.close()


if __name__ == '__main__':
    unittest.main()
