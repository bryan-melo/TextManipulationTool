import unittest

from text_manipulator.features.search_replace import search_replace


class TestSearchReplace(unittest.TestCase):
    def test_search_replace(self):
        self.assertEqual(search_replace('Hello, world!', 'Hello', 'Goodbye'),
                         'Goodbye, world!')
        self.assertEqual(search_replace('Today I walked, then I ran, then I showered, finally I slept.',
                                        'I', 'you'),
                         'Today you walked, then you ran, then you showered, finally you slept.')


if __name__ == '__main__':
    unittest.main()
