import unittest
from CTCI.ch1_4_palindrome_permutation import is_palindrome_permutation

class TestIsPalindromPermutation(unittest.TestCase):

    def test1(self):
        self.assertEqual(is_palindrome_permutation('Taco bCat'),True)


if __name__ == "__main__":
    unittest.main()