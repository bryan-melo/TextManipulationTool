import unittest

from text_manipulator.features.slicing import slicing


class TestSlicing(unittest.TestCase):
    def test_slicing(self):
        self.assertEqual(slicing('Hello, World!', 0, 5), 'Hello')
        self.assertEqual(slicing('Hello, World!', 5, 6), ',')


if __name__ == '__main__':
    unittest.main()
