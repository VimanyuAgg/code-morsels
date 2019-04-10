import unittest
from CTCI.ch16_8_english_int import numberToWords

class TestEnglishInt(unittest.TestCase):

    def test_zero(self):
        self.assertEqual(numberToWords(0),"Zero")


    def test_just_thousand(self):
        self.assertEqual(numberToWords(3000),"Three Thousand")

    def test_just_million(self):
        self.assertEqual(numberToWords(3000000),"Three Million")

    def test_no_hundred_tens_less_than19(self):
        self.assertEqual(numberToWords(4018),"Four Thousand Eighteen")

    def test_no_hundred_tens_greater_than19(self):
        self.assertEqual(numberToWords(4081),"Four Thousand Eighty One")

    def test_no_hundred_no_units(self):
        self.assertEqual(numberToWords(4080),"Four Thousand Eighty")

    def test_no_hundred_no_tens(self):
        self.assertEqual(numberToWords(4007),"Four Thousand Seven")

    def test_no_tens_no_units(self):
        self.assertEqual(numberToWords(4100),"Four Thousand One Hundred")

    def test_big_number(self):
        self.assertEqual(numberToWords(1234567891),"One Billion Two Hundred Thirty Four Million Five Hundred Sixty Seven Thousand Eight Hundred Ninety One")

    def test_negative(self):
        self.assertEqual(numberToWords(-3243),"Negative Three Thousand Two Hundred Forty Three")


if __name__ == "__main__":
    unittest.main()