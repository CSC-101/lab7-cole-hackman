from convert import str_to_float
import unittest

class TestCases(unittest.TestCase):

    def test_str_to_float_1(self):
        result = str_to_float("55.0")
        expected = 55.0
        self.assertEqual(result,expected)

    def test_str_to_float_2(self):
        result = str_to_float("This will fail")
        expected = None
        self.assertEqual(result,expected)

