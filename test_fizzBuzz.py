import sys
import unittest
import fizzBuzz

class FizzBuzzTest(unittest.TestCase):
    def test_fizzBuzz1(self):
        self.assertEqual(fizzBuzz.fizzBuzz(15), 'FizzBuzz')
    def test_fizzBuzz2(self):
        self.assertEqual(fizzBuzz.fizzBuzz(6), 'Fizz')
        
if __name__ == "__main__":
    unittest.main()  