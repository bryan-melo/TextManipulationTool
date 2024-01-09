import unittest
import os

from text_manipulator.document_handling.text_handling.text_handler import TextHandler


class TestTextHandler(unittest.TestCase):
    def setUp(self):
        # Create a temporary test file
        self.test_file_path = 'test_input.txt'
        with open(self.test_file_path, 'w') as test_file:
            test_file.write("Hello, World!\nThis is a test.")

        self.text_handler = TextHandler(self.test_file_path)

    def test_process_text(self):
        # Perform text processing
        self.text_handler.process_text()

        # Check if the output file is created
        self.assertTrue(os.path.exists('output.txt'))

        # Check the content of the output file
        with open('output.txt', 'r') as output_file:
            modified_content = output_file.read()
            self.assertEqual(modified_content, "Hello$$ World!\nThis is a test.")

    def tearDown(self):
        # Clean up the temporary test file and output file
        os.remove(self.test_file_path)
        os.remove('output.txt')


if __name__ == '__main__':
    unittest.main()
