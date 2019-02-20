from CTCI.ch16_18_pattern_match import pattern_match as pattern_match
import unittest

class TestPatternMatch(unittest.TestCase):

    def test1(self):
        self.assertEqual(pattern_match('aabab', 'cabcabgocabgo'),True)

    def test2(self):
        self.assertEqual(pattern_match('abab', 'cabgocabgo'),True)

    def test3(self):
        self.assertEqual(pattern_match('aa', 'cabcab'),True)

    def test4(self):
        self.assertEqual(pattern_match('aab', 'cabcab'),False)

    def test5(self):
        self.assertEqual(pattern_match('ab', 'cabcab'),True)

    def test6(self):
        self.assertEqual(pattern_match('a', 'cabcab'),True)

    def test7(self):
        self.assertEqual(pattern_match('', 'cabcab'),False)


if __name__=="__main__":
    unittest.main()