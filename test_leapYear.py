import unittest
import leapYear

class LeapYearTest(unittest.TestCase):
    def test_leapYear1(self):
        self.assertEqual(leapYear.leapYear(2003), False)

if __name__ == "__main__":
    unittest.main()  