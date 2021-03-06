import unittest
# from w1_sol import get_earliest_bonus
from w1_t2_get_earliest import get_earliest, get_earliest_bonus

imported_func = get_earliest

class GetEarliestTests(unittest.TestCase):

    """Tests for get_earliest."""

    def test_same_month_and_day(self):
        newer = "01/27/1832"
        older = "01/27/1756"
        self.assertEqual(imported_func(newer, older), older)
        print("Test 1 successful")

    def test_february_29th(self):
        newer = "02/29/1972"
        older = "12/21/1946"
        self.assertEqual(imported_func(newer, older), older)
        print("Test 2 successful")

    def test_smaller_month_bigger_day(self):
        newer = "03/21/1946"
        older = "02/24/1946"
        self.assertEqual(imported_func(older, newer), older)
        print("Test 3 successful")

    def test_same_month_and_year(self):
        newer = "06/24/1958"
        older = "06/21/1958"
        self.assertEqual(imported_func(older, newer), older)
        print("Test 4 successful")

    def test_invalid_date_allowed(self):
        newer = "02/29/2006"
        older = "02/28/2006"
        self.assertEqual(imported_func(older, newer), older)
        print("Test 5 successful")

    def test_two_invalid_dates(self):
        newer = "02/30/2006"
        older = "02/29/2006"
        self.assertEqual(imported_func(newer, older), older)
        print("Test 6 successful")

    # To test the Bonus part of this exercise, comment out the following line
    # @unittest.expectedFailure
    def test_many_dates(self):
        d1 = "01/24/2007"
        d2 = "01/21/2008"
        d3 = "02/29/2009"
        d4 = "02/30/2006"
        d5 = "02/28/2006"
        d6 = "02/29/2006"
        self.assertEqual(imported_func(d1, d2, d3), d1)
        self.assertEqual(imported_func(d1, d2, d3, d4), d4)
        self.assertEqual(imported_func(d1, d2, d3, d4, d5, d6), d5)
        print("Test 7 successful")


if __name__ == "__main__":
    unittest.main()