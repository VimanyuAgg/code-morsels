import unittest
from leetcode.longest_palindrome import longest_palindromic_substring_dp as longest_palindrome
import leetcode

class TestLongestPalindrome(unittest.TestCase):

    def test1(self):
        s = "babad"
        if longest_palindrome(s) in ["aba","bab"]:
            self.assertEqual(1,1)
        else:
            self.assertEqual(1,2)

    def test_null_str(self):
        s = None
        if longest_palindrome(s) in [""]:
            self.assertEqual(1,1)
        else:
            self.assertEqual(1,2)

        self.assertEqual(longest_palindrome(s), "")

    def test_empty_str(self):
        s = ""
        if longest_palindrome(s) in [""]:
            self.assertEqual(1,1)
        else:
            self.assertEqual(1,2)

        self.assertEqual(longest_palindrome(s), "")

    def test_nonpalindrome(self):
        s = "abc"
        if longest_palindrome(s) in ["a", "b", "c"]:
            self.assertEqual(1,1)
        else:
            self.assertEqual(1,2)


    def test2(self):
        s = "aaaaaab"
        if longest_palindrome(s) in ["aaaaaa"]:
            self.assertEqual(1,1)
        else:
            self.assertEqual(1,2)

    def test3(self):
        s = "abcdbb"

        if longest_palindrome(s) in ["bb"]:
            self.assertEqual(1,1)
        else:
            self.assertEqual(1,2)

    def test4(self):
        s = "aaabaaaa"

        if longest_palindrome(s) in ["aaabaaa"]:
            self.assertEqual(1,1)
        else:
            self.assertEqual(1,2)

    def test5(self):
        s = "abababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababa"

        self.assertEqual(leetcode.longest_palindrome.longest_palindrome_original(s), leetcode.longest_palindrome.longest_palindromic_substring_dp(s))

if __name__ == "__main__":
    unittest.main()