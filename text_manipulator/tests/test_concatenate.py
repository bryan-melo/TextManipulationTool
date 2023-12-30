import unittest

from text_manipulator.features.concatenate import concatenate_strings


class TestConcatenate(unittest.TestCase):

    def test_concatenate_strings(self):
        self.assertEqual(concatenate_strings('Hello, ', 'World!'), 'Hello, World!')
        self.assertEqual(concatenate_strings('Hello', ''), 'Hello')
        self.assertEqual(concatenate_strings('', 'World!'), 'World!')
        self.assertEqual(concatenate_strings('', ''), '')


if __name__ == '__main__':
    unittest.main()
