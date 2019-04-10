import unittest
from leetcode.longest_common_substring_val import longest_common_substring_val
class TestLongestCommonSubstrVal(unittest.TestCase):

    def test1(self):
        self.assertEqual(longest_common_substring_val("abad","bad"),"bad")

    def test2(self):
        self.assertEqual(longest_common_substring_val("abad","badass"),"bad")

    def test3(self):
        self.assertEqual(longest_common_substring_val("disjoint1","really"),"")


if __name__ == "__main__":
    unittest.main()