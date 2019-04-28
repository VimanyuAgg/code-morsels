import unittest
from CTCI.ch1_3_urlify import urlify


class TestUrlify(unittest.TestCase):

    def test1(self):
        s = "Mr John Smith    "
        self.assertEqual(urlify(s),"Mr%20John%20Smith")


if __name__ == "__main__":
    unittest.main()