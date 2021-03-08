import unittest
import leapYear

class LeapYearTest(unittest.TestCase):
    def test_leapYear1(self):
        self.assertEqual(leapYear.leapYear(2003), False)
    def test_leapYear2(self):
        self.assertEqual(leapYear.leapYear(2008), True)
    def test_leapYear3(self):
        self.assertEqual(leapYear.leapYear(2400), True)
    def test_leapYear4(self):
        self.assertEqual(leapYear.leapYear(2100), False)

if __name__ == "__main__":
    unittest.main()  