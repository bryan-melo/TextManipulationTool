# Test case for case_conversion.py
import unittest

from text_manipulator.features.case_conversion import all_uppercase_letters, all_lowercase_letters, capitalisation


class TestCaseConversion(unittest.TestCase):

    def test_all_uppercase_letters(self):
        self.assertEqual(all_uppercase_letters("Hello"), "HELLO")
        self.assertEqual(all_uppercase_letters(""), None)

    def test_all_lowercase_letters(self):
        self.assertEqual(all_lowercase_letters("HELLO"), "hello")
        self.assertEqual(all_lowercase_letters(""), None)

    def test_capitalisation(self):
        self.assertEqual(capitalisation("hello"), "Hello")
        self.assertEqual(capitalisation(""), None)


if __name__ == '__main__':
    unittest.main()
