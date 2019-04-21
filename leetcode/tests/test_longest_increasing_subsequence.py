import unittest
from leetcode.longest_increasing_subsequence import longest_increasing_subsequence

class TestLongestIncreasingSubsequence(unittest.TestCase):

    def test1(self):
        arr = [5, 7, 4, -3, 9, 1, 10, 4, 5, 8, 9, 3]
        self.assertEqual(longest_increasing_subsequence(arr), 6)


    def test2(self):
        arr = [5, 8, 3, 6, 9, 4, 10, 5, 6, 7]
        self.assertEqual(longest_increasing_subsequence(arr), 5)


if __name__ == "__main__":
    unittest.main()