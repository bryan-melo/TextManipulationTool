import unittest

from text_manipulator.features.text_manipulation import TextManipulation


class TestTextManipulation(unittest.TestCase):
    def setUp(self):
        self.text_manipulator = TextManipulation("Hello, World!")

    def test_all_uppercase_letters(self):
        self.assertEqual(self.text_manipulator.all_uppercase_letters(), "HELLO, WORLD!")

    def test_all_lowercase_letters(self):
        self.assertEqual(self.text_manipulator.all_lowercase_letters(), "hello, world!")

    def test_capitalisation(self):
        self.assertEqual(self.text_manipulator.capitalisation(), "Hello, world!")

    def test_concatenate_string(self):
        self.assertEqual(self.text_manipulator.concatenate_string(" How are you?"), "Hello, World! How are you?")

    def test_search_replace(self):
        self.assertEqual(self.text_manipulator.search_replace("Hello", "Goodbye"), "Goodbye, World!")

    def test_substring(self):
        self.assertEqual(self.text_manipulator.substring(7, None), "World!")


if __name__ == '__main__':
    unittest.main()


