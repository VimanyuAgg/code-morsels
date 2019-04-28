import unittest
from CTCI.ch1_1_isunique import is_unique


class TestIsUnique(unittest.TestCase):


    def test_lowerCaseString(self):
        s = "howisteday"
        self.assertEqual(is_unique(s),True)


if __name__ == "__main__":
    unittest.main()