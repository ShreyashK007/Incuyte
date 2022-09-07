import unittest
from . assesment import StringCalculator

class simpletest(unittest.TestCase):

    def test_blank_num_add(self):
        result = StringCalculator().add("")
        self.assertEqual(result, 0)
    
    def test_single_num_add(self):
        result = StringCalculator().add("1")
        self.assertEqual(result, 1)

    def test_2_num_add(self):
        result = StringCalculator().add("1,2")
        self.assertEqual(result, 3)

    def test_mult_num_add(self):
        res = StringCalculator().add("1,2,3")
        self.assertEqual(res, 1 + 2 + 3)

if __name__ == '__main__':
    unittest.main()