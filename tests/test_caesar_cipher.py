import unittest
from caesar_cipher import caesar_cipher

class TestCaesarCipher(unittest.TestCase):
    def test_basic(self):
        self.assertEqual(caesar_cipher("abc", 1), "bcd")
        self.assertEqual(caesar_cipher("xyz", 3), "abc")
        self.assertEqual(caesar_cipher("AbC", 2), "CdE")
        self.assertEqual(caesar_cipher("Hello, World!", 5), "Mjqqt, Btwqi!")

if __name__ == "__main__":
    unittest.main()