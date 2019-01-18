# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import unittest


# from w2_count import count_words
from w2_t2_count_words import count_words_m1, count_words_m2, count_words_m3

imported_func = count_words_m3

class CountWordsTests(unittest.TestCase):

    """Tests for count_words."""

    def test_simple_sentence(self):
        actual = imported_func("oh what a day what a lovely day")
        expected = {'oh': 1, 'what': 2, 'a': 2, 'day': 2, 'lovely': 1}
        self.assertEqual(actual, expected)

    def test_apostrophe(self):
        actual = imported_func("don't stop believing")
        expected = {"don't": 1, 'stop': 1, 'believing': 1}
        self.assertEqual(actual, expected)

    # To test the Bonus part of this exercise, comment out the following line
    # @unittest.expectedFailure
    def test_capitalization(self):
        actual = imported_func("Oh what a day what a lovely day")
        expected = {'oh': 1, 'what': 2, 'a': 2, 'day': 2, 'lovely': 1}
        self.assertEqual(actual, expected)

    # To test the Bonus part of this exercise, comment out the following line
    # @unittest.expectedFailure
    def test_symbols(self):
        actual = imported_func("Oh what-- a day, what a lovely day!")
        expected = {'oh': 1, 'what': 2, 'a': 2, 'day': 2, 'lovely': 1}
        self.assertEqual(actual, expected)
        actual = imported_func("¿Te gusta Python?")
        expected = {'te': 1, 'gusta': 1, 'python': 1}
        self.assertEqual(actual, expected)


if __name__ == "__main__":
    unittest.main()