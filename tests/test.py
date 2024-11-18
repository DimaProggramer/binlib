# tests/test.py

import unittest
from binlib import text_to_binary, binary_to_text, is_valid_binary, clean_binary

class TestBinaryLibrary(unittest.TestCase):

    def test_text_to_binary(self):
        self.assertEqual(text_to_binary("Hello"), "01001000 01100101 01101100 01101100 01101111")
        self.assertEqual(text_to_binary("Hi"), "01001000 01101001")

    def test_binary_to_text(self):
        self.assertEqual(binary_to_text("01001000 01100101 01101100 01101100 01101111"), "Hello")
        self.assertEqual(binary_to_text("01001000 01101001"), "Hi")

    def test_is_valid_binary(self):
        self.assertTrue(is_valid_binary("01001000 01100101 01101100 01101100 01101111"))
        self.assertFalse(is_valid_binary("01001000 011001Z 01101100 01101100 01101111"))
        self.assertFalse(is_valid_binary("Hello"))

    def test_clean_binary(self):
        self.assertEqual(clean_binary("01001000   01100101"), "01001000 01100101")
        self.assertEqual(clean_binary(" 01001000  01100101 "), "01001000 01100101")

    def test_invalid_binary_to_text(self):
        with self.assertRaises(ValueError):
            binary_to_text("01001000 0110010x 01101100")
        
if __name__ == "__main__":
    unittest.main()
