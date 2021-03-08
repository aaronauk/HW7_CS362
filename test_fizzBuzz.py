import sys
import unittest
import fizzBuzz

class FizzBuzzTest(unittest.TestCase):
    def test_fizzBuzz1(self):
        self.assertEqual(fizzBuzz.fizzBuzz(15), 'FizzBuzz')

if __name__ == "__main__":
    unittest.main()  