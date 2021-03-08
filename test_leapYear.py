import unittest
import leapYear

class LeapYearTest(unittest.TestCase):
    def test_leapYear1(self):
        self.assertEqual(leapYear.leapYear(2003), False)
    def test_leapYear2(self):
        self.assertEqual(leapYear.leapYear(2008), True)
        
if __name__ == "__main__":
    unittest.main()  