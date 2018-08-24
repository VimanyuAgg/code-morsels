# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import unittest


from w2_count_words_attempt2 import count_words, count_words_bonus


class CountWordsTests(unittest.TestCase):

    """Tests for count_words."""

    def test_simple_sentence(self):
        actual = count_words_bonus("oh what a day what a lovely day")
        expected = {'oh': 1, 'what': 2, 'a': 2, 'day': 2, 'lovely': 1}
        self.assertEqual(actual, expected)

    def test_apostrophe(self):
        actual = count_words_bonus("don't stop believing")
        expected = {"don't": 1, 'stop': 1, 'believing': 1}
        self.assertEqual(actual, expected)

    # To test the Bonus part of this exercise, comment out the following line
    # @unittest.expectedFailure
    def test_capitalization(self):
        actual = count_words_bonus("Oh what a day what a lovely day")
        expected = {'oh': 1, 'what': 2, 'a': 2, 'day': 2, 'lovely': 1}
        self.assertEqual(actual, expected)

    # To test the Bonus part of this exercise, comment out the following line
    # @unittest.expectedFailure
    def test_symbols(self):
        actual = count_words_bonus("Oh what a day, what a lovely day!")
        expected = {'oh': 1, 'what': 2, 'a': 2, 'day': 2, 'lovely': 1}
        actual = count_words_bonus("¿Te gusta Python?")
        expected = {'te': 1, 'gusta': 1, 'python': 1}
        self.assertEqual(actual, expected)


if __name__ == "__main__":
    unittest.main()