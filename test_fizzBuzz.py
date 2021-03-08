import sys
import unittest
import fizzBuzz

class FizzBuzzTest(unittest.TestCase):
    def test_fizzBuzz1(self):
        self.assertEqual(fizzBuzz.fizzBuzz(15), 'FizzBuzz')
    def test_fizzBuzz2(self):
        self.assertEqual(fizzBuzz.fizzBuzz(6), 'Fizz')
    def test_fizzBuzz3(self):
        self.assertEqual(fizzBuzz.fizzBuzz(10), 'Buzz')
    def test_fizzBuzz4(self):
        self.assertEqual(fizzBuzz.fizzBuzz(2), 2)
    def test_fizzBuzz5(self):
        self.assertEqual(fizzBuzz.fizzBuzz(105), None)

if __name__ == "__main__":
    unittest.main()  