import unittest
from leetcode.longest_common_subsequence import longest_common_subsequence, backtrack_common_subsequence

class TestLongestCommonSubsequence(unittest.TestCase):

    def test1 (self):
        arr1 = "ABDABDL"
        arr2 = "CBADKJBBBDL"
        self.assertEqual(longest_common_subsequence(arr1, arr2)[0], 5)
        self.assertEqual(backtrack_common_subsequence(arr1, arr2), 'BABDL')

    def test2 (self):
        arr1 = ""
        arr2 = "CBADKJBBBDL"
        self.assertEqual(longest_common_subsequence(arr1, arr2)[0], 0)
        self.assertEqual(backtrack_common_subsequence(arr1, arr2), '')

if __name__ == "__main__":
    unittest.main()
